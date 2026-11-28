#!/usr/bin/env python3
"""XP moyenne par poireau, mode et résultat, à partir des combats en cache (fights/*.json).

Usage : python3 tools/xp_stats.py [ids…]   (sans argument : tous les combats en cache)
Les entraînements (context 0) sont exclus : ils ne rapportent pas d'XP.
"""
import json
import pathlib
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
MINE = {"KrazyKlick", "KrazyKeel"}
TYPES = {0: "solo", 1: "éleveur", 2: "équipe", 6: "battle royale", 7: "battle royale (tournoi)"}


def main(argv):
    paths = [ROOT / "fights" / f"{i}.json" for i in argv] or sorted((ROOT / "fights").glob("*.json"))
    stats = defaultdict(list)
    for p in paths:
        f = json.loads(p.read_text())
        r = f.get("report")
        if not r or f.get("context") == 0:
            continue
        for side, team in (("leeks1", 1), ("leeks2", 2)):
            for l in r[side]:
                if l["name"] in MINE:
                    res = "nul" if f["winner"] <= 0 else ("victoire" if f["winner"] == team else "défaite")
                    stats[(l["name"], TYPES.get(f["type"], f"type {f['type']}"), res)].append((l["xp"], l["level"]))
    print(f"{'Poireau':11} {'Mode':24} {'Résultat':9} {'n':>3} {'XP moy.':>8} {'min–max':>11} niveaux")
    for (name, mode, res), v in sorted(stats.items()):
        xp = [x for x, _ in v]
        lv = sorted({lvl for _, lvl in v})
        print(f"{name:11} {mode:24} {res:9} {len(v):>3} {sum(xp) / len(xp):>8.0f} {min(xp):>5}–{max(xp):<5} {lv[0]}–{lv[-1]}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
