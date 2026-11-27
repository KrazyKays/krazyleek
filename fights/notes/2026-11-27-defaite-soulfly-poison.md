# Défaite contre SoulFly777 (niv. 50, build poison) — 54978580

**Verdict : MIXTE** (écart +7, mais erreurs IA).

- Lui : **force 0**, magie élevée ; double pistolet (poison), Venin, soins, bouclier, mur, bottes.
  **794 de nos 815 PV perdus en poison** (ignore les boucliers) ; ses coups directs font 0–10.
- Nous : 232 infligés. T2 : Solidification + Bouclier + casque (13 PT) **inutiles** ; T6 bouclier inutile.
  T3/T4 : tours vides au contact (ancienne approche ; corrigé par la mise à jour non encore installée).

## Correction
- `enemyHitProfile` : [coups par tour, dégâts directs par coup]. Valeur d'un bouclier =
  min(bouclier, dégâts par coup) × coups × durée. Si les coups font < 10 : aucun bouclier
  (ni dans le plan, ni avec les PT restants).
- `analyze_fight.py` affiche science et magie.

## Contre le poison (à retenir)
Le poison s'empile : plus le combat dure, plus on perd. Il faut **conclure vite** (aller au contact,
tout en dégâts) plutôt que se protéger. Libération (niv. 60) retire une partie des effets.
