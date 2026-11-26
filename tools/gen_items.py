#!/usr/bin/env python3
"""Génère ai/lib/items.leek à partir de docs/data/ (données officielles de l'API).

Usage : python3 tools/gen_items.py
Deux maps (les ids d'armes et de puces peuvent se chevaucher) : WEAPON_DATA et CHIP_DATA.
Chaque entrée :
  [coût PT, portée min, portée max, type de lancer, ligne de vue (bool),
   utilisations max/tour (-1 = illimité), recharge, dégâts moyens de base (somme des effets
   de dégâts), nombre d'effets de dégâts, soin moyen de base, zone (1 = une seule case)]
Les dégâts/soins sont les valeurs de base (avant force/sagesse) : moyenne value1 + value2/2.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "data"
OUT = ROOT / "ai" / "lib" / "items.leek"
EFFECT_DAMAGE, EFFECT_HEAL = 1, 2


def row(item, cooldown):
    dmg = [e for e in item["effects"] if e["id"] == EFFECT_DAMAGE]
    heal = [e for e in item["effects"] if e["id"] == EFFECT_HEAL]
    avg = lambda effects: sum(e["value1"] + e["value2"] / 2 for e in effects)
    return [item["cost"], item["min_range"], item["max_range"], item["launch_type"],
            "true" if item["los"] else "false", item["max_uses"], cooldown,
            avg(dmg), len(dmg), avg(heal), item["area"]]


def main():
    constants = {c["name"]: c["value"] for c in json.loads((DATA / "constants.json").read_text())["constants"]}
    by_value = {}
    for name, value in constants.items():
        if name.startswith(("WEAPON_", "CHIP_")):
            by_value.setdefault((name.split("_")[0], str(value)), name)

    weapons = json.loads((DATA / "weapons.json").read_text())["weapons"].values()
    chips = json.loads((DATA / "chips.json").read_text())["chips"].values()
    weapon_rows = sorted((by_value[("WEAPON", str(w["item"]))], row(w, 0))
                         for w in weapons if ("WEAPON", str(w["item"])) in by_value)
    chip_rows = sorted((by_value[("CHIP", str(c["id"]))], row(c, c["cooldown"]))
                       for c in chips if ("CHIP", str(c["id"])) in by_value)

    def block(name, rows):
        out = [f"global {name} = ["]
        out += [f"    {const}: [{', '.join(str(v) for v in r)}]," for const, r in rows]
        out[-1] = out[-1].rstrip(",")
        return out + ["];", ""]

    lines = ["// FICHIER GÉNÉRÉ par tools/gen_items.py — ne pas modifier à la main.",
             "// [coût, porteeMin, porteeMax, lancer, lignedevue, maxUtil, recharge, degatsMoy, nbDegats, soinMoy, zone]",
             ""]
    lines += block("WEAPON_DATA", weapon_rows) + block("CHIP_DATA", chip_rows)
    entries = weapon_rows + chip_rows
    lines += ["// Index des colonnes",
              "global I_COST = 0; global I_MIN = 1; global I_MAX = 2; global I_LAUNCH = 3; global I_LOS = 4;",
              "global I_USES = 5; global I_CD = 6; global I_DMG = 7; global I_HITS = 8; global I_HEAL = 9; global I_AREA = 10;",
              ""]
    OUT.write_text("\n".join(lines))
    print(f"{len(entries)} objets -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
