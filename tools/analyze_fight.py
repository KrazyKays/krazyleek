#!/usr/bin/env python3
"""Analyse un combat Leek Wars : déroulé tour par tour, PT gaspillés, dégâts.

Usage : python3 tools/analyze_fight.py <id ou URL> [--me NOM]   (défaut : KrazyKlick)
Termine par un DIAGNOSTIC : défaite évitable (erreurs de l'IA) ou due à l'écart de niveau / d'équipement.
Le JSON est mis en cache dans fights/<id>.json (ignoré par git).
Décodage des actions établi empiriquement (combats 54965116, 54966254) :
  6 nouveau tour | 7 début du tour d'une entité | 8 fin [entité, PT total, PM total]
  10 déplacement [entité, case, chemin] | 12 puce [modèle, case, résultat]
  13 changement d'arme [modèle] | 16 tir [case, résultat] | 101 PV perdus [entité, valeur, érosion]
  103 soin [entité, valeur] | 302 effet [objet, id, lanceur, cible, ?, type, valeur, tours]
  303 fin d'effet [id] | 203 message | 5 mort [entité, tueur] | 110 poison [entité, valeur, érosion]
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
    my_name = argv[argv.index("--me") + 1] if "--me" in argv else "KrazyKlick"
    me = next((i for i, l in leeks.items() if l["name"].lower() == my_name.lower()), 0)
    foes = [i for i, l in leeks.items() if l["team"] != leeks[me]["team"] and not l.get("summon")]
    foe = foes[0] if foes else None

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
    engaged_idle = []   # tours où l'on garde >= 5 PT alors que l'adversaire est à <= 8 cases
    healed = {i: 0 for i in leeks}
    poison = {}
    used_chips = {i: set() for i in leeks}
    weapon = {i: None for i in leeks}
    tp_total = {i: l["tp"] for i, l in leeks.items()}
    line = []

    def flush(entity, tp):
        nonlocal line
        left = tp - spent
        d = min((distance(pos[me], pos[f], width) for f in foes), default="?")
        if entity == me and left > 0:
            wasted.append((turn, left))
            if left >= 5 and d != "?" and d <= 8:
                engaged_idle.append((turn, left, d))
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
            used_chips[current].add(name)
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
        elif code == 110:  # dégâts de poison [cible, valeur, érosion] (ignorent les boucliers)
            taken[a[1]] += a[2]
            poison[a[1]] = poison.get(a[1], 0) + a[2]
            others = [i for i in leeks if leeks[i]["team"] != leeks[a[1]]["team"] and not leeks[i].get("summon")]
            if len(others) == 1:
                dealt[others[0]] += a[2]
            line.append(f"poison [{a[2]}]")
        elif code == 103:
            healed[a[1]] = healed.get(a[1], 0) + a[2]
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
    for i, v in poison.items():
        print(f"Dont poison subi par {names[i]} : {v}")
    print(f"Opérations : {data.get('ops')}")
    if foe is not None:
        diagnose(fight, leeks, me, foe, dealt, taken, healed, used_chips, engaged_idle)
    return 0


DEFENSIVE = {"shield", "helmet", "solidification", "armor", "wall"}


def diagnose(fight, leeks, me, foe, dealt, taken, healed, used_chips, engaged_idle):
    """Classe le résultat : évitable (erreurs IA) / écart de niveau / build."""
    chips = {c["id"]: c for c in json.loads((DATA / "chips.json").read_text())["chips"].values()}
    weapons = {w["item"]: w for w in json.loads((DATA / "weapons.json").read_text())["weapons"].values()}
    m, f = leeks[me], leeks[foe]
    won = fight["winner"] == m["team"]
    draw = fight["winner"] <= 0
    gap = f.get("level", 0) - m.get("level", 0)
    foe_left = max(0, f["life"] - taken[foe] + healed.get(foe, 0))
    my_items = {chips[c]["name"] for c in m["equipment"]["chips"] if c in chips}
    foe_items = ({chips[c]["name"] for c in f["equipment"]["chips"] if c in chips}
                 | {weapons[w]["name"] for w in f["equipment"]["weapons"] if w in weapons})
    my_weapons = {weapons[w]["name"] for w in m["equipment"]["weapons"] if w in weapons}

    signals = []
    if engaged_idle:
        signals.append("tours vides au contact : " + ", ".join(f"T{t} ({p} PT, {d} cases)" for t, p, d in engaged_idle))
    if dealt[me] == 0:
        signals.append("aucun dégât infligé (ciblage / déplacement)")
    if draw:
        signals.append("match nul : on n'a pas réussi à conclure")
    unused_def = (my_items & DEFENSIVE) - used_chips[me]
    if not won and unused_def and taken[me] >= m["life"] * 0.5:
        signals.append("puces défensives jamais lancées : " + ", ".join(sorted(unused_def)))
    close = not won and not draw and foe_left <= f["life"] * 0.25

    print("\n=== DIAGNOSTIC ===")
    print(f"Niveaux : {m['name']} {m.get('level')} vs {f['name']} {f.get('level')} (écart {gap:+d})")
    print(f"Stats adverses vs nous : PV {f['life']}/{m['life']}, force {f['strength']}/{m['strength']}, "
          f"résistance {f['resistance']}/{m['resistance']}, PT {f['tp']}/{m['tp']}, PM {f['mp']}/{m['mp']}, "
          f"fréquence {f['frequency']}/{m['frequency']}")
    print(f"PV adverses restants (estimation) : {foe_left}/{f['life']}" + (" → défaite serrée" if close else ""))
    notable = sorted(foe_items - my_items - my_weapons)
    if notable:
        print("Objets adverses que nous n'avons pas : " + ", ".join(notable))
    if won:
        verdict = "VICTOIRE" + (" — points à améliorer ci-dessous" if signals else "")
    elif signals and gap >= 5:
        verdict = "MIXTE : écart de niveau, MAIS erreurs de l'IA à corriger"
    elif signals:
        verdict = "ÉVITABLE : erreurs de l'IA"
    elif gap >= 5:
        verdict = "ÉCART DE NIVEAU : pas d'erreur flagrante, l'adversaire est simplement plus avancé"
    else:
        verdict = "NIVEAU PROCHE, SANS ERREUR FLAGRANTE : regarder le build / l'équipement adverse"
    print("Verdict : " + verdict)
    for s in signals:
        print("  - " + s)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
