# 55025102, 55026064 (éleveur), 55026142 (solo krazyKlick), 55026213 (solo KrazyKeel) — 4 VICTOIRES

- Éleveur (2 c 2) : krazyKlick fait tout (1 032 et 1 218 dégâts) ; KrazyKeel (3 PM) n'arrive jamais à portée
  (12–15 cases quand le combat se joue) : 0 dégât, 9–10 XP.
- 55026142 : krazyKlick bat PAX53 (niv. 50) en 6 tours, 6 PT perdus → **710 XP, passage au niveau 52**.
- 55026213 : KrazyKeel attend 2 tours à 11 cases (T5–T6, `HOLD_COUNT`), s'avance, tire en premier : 100–0, 16 XP.
- Outil : `analyze_fight.py` calculait la colonne « dist » depuis notre poireau pour toutes les lignes ;
  corrigé (distance de l'entité qui joue à son adversaire le plus proche).

## XP par combat (tools/xp_stats.py, 2026-11-28)
| | Solo victoire | Solo défaite | Éleveur victoire |
|---|---|---|---|
| krazyKlick | 688 (n = 2) | 148 (n = 19) | 170 (n = 2) |
| KrazyKeel | 16 (n = 1) | ? | 10 (n = 2) |
→ Un combat éleveur rapporte ≈ 180 XP au total ; un solo krazyKlick 148 au pire, ≈ 690 en cas de victoire.
**Le solo est plus rentable pour les deux poireaux.**
