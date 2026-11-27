#!/usr/bin/env python3
"""Analyse un combat Leek Wars : déroulé tour par tour, PT gaspillés, dégâts.

Usage : python3 tools/analyze_fight.py <id ou URL> [--me NOM]
Le JSON est mis en cache dans fights/<id>.json (ignoré par git).
Décodage des actions établi empiriquement (combats 54965116, 54966254) :
  6 nouveau tour | 7 début du tour d'une entité | 8 fin [entité, PT total, PM total]
  10 déplacement [entité, case, chemin] | 12 puce [modèle, case, résultat]
  13 changement d'arme [modèle] | 16 tir [case, résultat] | 101 PV perdus [entité, valeur, érosion]
  103 soin [entité, valeur] | 302 effet [objet, id, lanceur, cible, ?, type, valeur, tours]
  303 fin d'effet [id] | 203 message | 5 mort [entité, tueur]
"""
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "data"
CACHE = ROOT / "fights"


def load_fight(arg):
    fight_id = re.findall(r"\d+", arg)[-1]
    path = CACHE / f"{fight_id}.json"
    if not path.exists() or json.loads(path.read_text()).get("status") != 2:
        with urllib.request.urlopen(f"https://leekwars.com/api/fight/get/{fight_id}", timeout=30) as r:
            path.write_bytes(r.read())
    return json.loads(path.read_text())


def item_tables():
    chips = json.loads((DATA / "chips.json").read_text())["chips"].values()
    weapons = json.loads((DATA / "weapons.json").read_text())["weapons"].values()
    chip_by_tpl = {c["template"]: c for c in chips}
    weapon_by_tpl = {w["template"]: w for w in weapons}
    weapon_by_item = {w["item"]: w for w in weapons}
    return chip_by_tpl, weapon_by_tpl, weapon_by_item


def distance(a, b, width):
    """Distance de Manhattan sur la grille en losange (voisins : ±(w-1), ±w)."""
    delta, best = b - a, None
    for s in range(-60, 61):
        du = delta - (width - 1) * s
        dv = s - du
        m = abs(du) + abs(dv)
        best = m if best is None or m < best else best
    return best


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    fight = load_fight(argv[0])
    if fight.get("status") != 2:
        print("Combat pas encore joué (en file d'attente).")
        return 1
    data = fight["data"]
    chip_by_tpl, weapon_by_tpl, weapon_by_item = item_tables()
    width = data["map"]["width"]
    leeks = {l["id"]: l for l in data["leeks"]}
    names = {i: l["name"] for i, l in leeks.items()}
    pos = {i: l["cellPos"] for i, l in leeks.items()}
    me = next((i for i, l in leeks.items() if len(argv) > 2 and l["name"] == argv[2]), 0)

    print(f"Combat {fight['id']} — gagnant : équipe {fight['winner']} "
          f"({'victoire' if fight['winner'] == leeks[me]['team'] else 'défaite' if fight['winner'] > 0 else 'nul'})")
    for l in leeks.values():
        eq = l.get("equipment", {})
        w = [weapon_by_item[x]["name"] for x in eq.get("weapons", []) if x in weapon_by_item]
        print(f"  {l['name']:12} PV {l['life']} F {l['strength']} Sa {l['wisdom']} Ag {l['agility']} "
              f"Ré {l['resistance']} Fr {l['frequency']} PT {l['tp']} PM {l['mp']} | armes {w}")
    print()

    turn, current, spent = 1, None, 0
    dealt = {i: 0 for i in leeks}
    taken = {i: 0 for i in leeks}
    wasted = []
    weapon = {i: None for i in leeks}
    tp_total = {i: l["tp"] for i, l in leeks.items()}
    line = []

    def flush(entity, tp):
        nonlocal line
        left = tp - spent
        if entity == me and left > 0:
            wasted.append((turn, left))
        foes = [i for i, l in leeks.items() if l["team"] != leeks[me]["team"] and not l.get("summon")]
        d = min((distance(pos[me], pos[f], width) for f in foes), default="?")
        print(f"T{turn:<2} {names[entity]:12} case {pos[entity]:>3} dist {d:>2} | "
              f"{', '.join(line) or '—'} | PT non utilisés : {left}")
        line = []

    for a in data["actions"]:
        code = a[0]
        if code == 6:
            turn = a[1]
        elif code == 7:
            current, spent = a[1], 0
        elif code == 8:
            tp_total[a[1]] = a[2]
            flush(a[1], a[2])
        elif code == 10:
            moved = len(a[3]) if isinstance(a[3], list) else 0
            pos[a[1]] = a[2]
            line.append(f"bouge {moved}")
        elif code == 12:
            chip = chip_by_tpl.get(a[1])
            name = chip["name"] if chip else f"puce#{a[1]}"
            spent += chip["cost"] if chip else 0
            line.append(name + ("" if a[3] > 0 else " (échec)"))
        elif code == 13:
            weapon[current] = weapon_by_tpl.get(a[1])
            spent += 1
            line.append("arme→" + (weapon[current]["name"] if weapon[current] else str(a[1])))
        elif code == 16:
            w = weapon[current]
            spent += w["cost"] if w else 0
            line.append((w["name"] if w else "tir") + ("" if a[2] > 0 else " (échec)"))
        elif code == 101:
            taken[a[1]] += a[2]
            if current is not None and current != a[1]:
                dealt[current] += a[2]
            line[-1:] = [f"{line[-1]} [{a[2]}]"] if line else []
        elif code == 103:
            line.append(f"+{a[2]} PV")
        elif code == 5:
            line.append(f"MORT de {names.get(a[1], a[1])}")

    print()
    for i in leeks:
        print(f"{names[i]:12} dégâts infligés {dealt[i]:>5} | subis {taken[i]:>5}")
    if wasted:
        total = sum(w for _, w in wasted)
        print(f"PT non utilisés par {names[me]} : {total} au total — " +
              ", ".join(f"T{t}:{w}" for t, w in wasted))
    print(f"Opérations : {data.get('ops')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
