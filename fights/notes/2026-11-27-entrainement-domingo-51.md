# 54994327 et 54994330 — entraînement contre Domingo (bot, niv. 51) : 2 VICTOIRES (0 XP, entraînement)

- 54994327 : propre. T3 flamme + Stalactite (353), T4 mitraillette ×3 (438) → mort de Domingo ; 11 PV subis.
- 54994330 : victoire 673–524 mais **T3–T4 : 13 PT perdus à 16 cases** (3 puis 2 cases parcourues, distance
  inchangée). Cause : `holdOutsideReach` choisissait sa case « à vol d'oiseau » même loin de la limite de
  portée → impasse contre les murs. **Correction** : loin de sa portée (distance > sa portée + ses PM + nos PM),
  approche normale par le vrai chemin ; l'attente ne joue qu'à la limite.
- T6–T8 : étincelles seules (5–30) à 3–8 cases, sans ligne de vue pour le reste ; acceptable.
