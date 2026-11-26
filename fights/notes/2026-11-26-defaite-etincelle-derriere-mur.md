# Défaite contre Prunaux — étincelle à travers un mur

- Lien : https://leekwars.com/fight/54965116 (graine 611240540)
- Adversaire : Prunaux niv. 32 — **293 PV**, force 70, sagesse 30, 12 PT, 4 PM, 20 cœurs.
  Fusil à pompe ; puces choc, bandage, soin, étincelle, caillou, casque.
- Nous : krazyKlick niv. 32 — 653 PV, mitraillette + pistolet, bandage/flamme/éclair/protéines/motivation/caillou.
- Résultat : défaite au tour 16. **Nous n'avons attaqué aucune fois.**

## Ce qui s'est passé
- T1–T4 : approche des deux côtés.
- Dès T5 : l'adversaire lance 4 étincelles par tour (12 PT) ≈ 80 dégâts, sans ligne de vue,
  en restant derrière un obstacle à 4–5 cases.
- Nous : bandage (≈ 25 PV) puis oscillation entre les cases 162 et 180 pendant 10 tours.

## Causes (bugs de l'IA)
1. `approachSafely` minimisait la distance de Manhattan en évitant d'être visible :
   bloqué au point le plus proche derrière le mur (minimum local), sans jamais contourner.
2. `retreatFrom` était appelé même sans avoir attaqué : il annulait l'approche → oscillation.
3. Après l'approche, l'attaque n'était retentée que si la meilleure case était la case actuelle.
4. Se cacher est inutile contre l'étincelle (pas de ligne de vue nécessaire).

## Corrections
- Approche par vrai chemin vers les positions d'attaque officielles (`getCellsToUseWeapon/Chip`
  + `moveTowardCells`), puis réévaluation complète avec les PM restants.
- Repli seulement après avoir frappé.
- Vérifications officielles (`canUseWeapon`/`canUseChip`) depuis la case actuelle.
- Log `[plan]` à chaque tour pour diagnostiquer.

## À retenir
Avec 293 PV en face et ~250 dégâts/tour, aller au contact gagnait en 2 tours.
