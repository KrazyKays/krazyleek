#!/usr/bin/env python3
"""Ce qui se débloque entre deux niveaux : armes, puces (marché) et composants.

Usage : python3 tools/unlocks.py <niveau_depuis> <niveau_jusqu_a> [--force N] [--sagesse N] [--resistance N]
Exemple : python3 tools/unlocks.py 42 50 --force 220
Pour chaque objet : coût, portée, effets clés et, pour les dégâts, dégâts moyens et dégâts/PT
avec la force donnée (formule officielle : base × (1 + force/100)).
À utiliser à chaque montée de niveau pour proposer un nouveau setup (voir CLAUDE.md).
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "data"
EFFECTS = {1: "dégâts", 2: "soin", 5: "bouclier relatif %", 6: "bouclier absolu", 13: "poison",
           14: "invocation", 16: "mort", 17: "entrave PM", 18: "entrave PT", 19: "entrave force",
           26: "vulnérabilité %", 27: "vulnérabilité absolue", 30: "dégâts nova", 31: "+PM", 32: "+PT",
           37: "bouclier absolu brut", 38: "+force", 40: "+science", 41: "+agilité", 42: "+résistance",
           44: "+sagesse", 9: "débuff (Libération)", 10: "téléportation", 12: "+PV max", 45: "nova vitalité",
           20: "renvoi de dégâts", 61: "vol de vie"}
LAUNCH = {1: "ligne", 2: "diagonale", 3: "étoile", 7: "cercle"}


def arg(name, default):
    return float(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    strength, wisdom, res = arg("--force", 220), arg("--sagesse", 0), arg("--resistance", 0)
    items = json.loads((DATA / "items.json").read_text())
    market = {v["name"]: v for v in items.values() if v.get("market") and v.get("price")}
    chips = json.loads((DATA / "chips.json").read_text())["chips"].values()
    weapons = json.loads((DATA / "weapons.json").read_text())["weapons"].values()

    rows = []
    for kind, prefix, objs in (("arme", "weapon_", weapons), ("puce", "chip_", chips)):
        for o in objs:
            item = market.get(prefix + o["name"])
            if not item or not (lo < o["level"] <= hi):
                continue
            dmg = sum(e["value1"] + e["value2"] / 2 for e in o["effects"] if e["id"] == 1) * (1 + strength / 100)
            heal = sum(e["value1"] + e["value2"] / 2 for e in o["effects"] if e["id"] == 2) * (1 + wisdom / 100)
            effects = []
            for e in o["effects"]:
                label = EFFECTS.get(e["id"], f"effet {e['id']}")
                val = e["value1"] if not e["value2"] else f"{e['value1']}–{e['value1'] + e['value2']}"
                effects.append(f"{label} {val}" + (f" ({e['turns']} t)" if e["turns"] > 0 else ""))
            rows.append((o["level"], kind, o["name"], o["cost"], f"{o['min_range']}–{o['max_range']}",
                         LAUNCH.get(o["launch_type"], o["launch_type"]), "oui" if o["los"] else "non",
                         o.get("cooldown", 0), round(dmg) if dmg else "", round(dmg / o["cost"], 1) if dmg else "",
                         round(heal) if heal else "", "; ".join(effects), item["price"]))

    print(f"Armes et puces du marché débloquées entre les niveaux {lo + 1} et {hi} "
          f"(force {strength:g}, sagesse {wisdom:g}) :\n")
    print("| Niv | Type | Objet | PT | Portée | Lancer | LdV | Rech. | Dégâts moy. | Dégâts/PT | Soin | Effets | Prix |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(rows):
        print("| " + " | ".join(str(x) for x in r) + " |")

    comps = json.loads((DATA / "components.json").read_text())["components"]
    sel = [c for c in comps if lo < c["level"] <= hi]
    if sel:
        print("\nComposants débloqués :\n")
        print("| Niv | Composant | Apports | Recette |")
        print("|---|---|---|---|")
        for c in sel:
            print(f"| {c['level']} | {c['name']} | {', '.join(c['gives'])} | {c['recipe']} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
