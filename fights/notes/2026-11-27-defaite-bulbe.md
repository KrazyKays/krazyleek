# Défaite contre Tezcatlioca (invocateur) — 54977534

- Lui : 391 PV, **force 345**, fréquence 150, 12 PT, 4 PM ; épée large + magnum, bulbe chétif, éclair, flamme,
  étincelle, protéines, bouclier, casque ; 8 composants.
- Nous : 723 PV, laser + mitraillette, Solidification équipée. **0 dégât infligé**, mort au tour 5 (776 subis).

## Cause
`chooseTarget` choisissait l'ennemi aux PV les plus bas : le **bulbe** (90 PV), resté loin derrière.
Le poireau a passé 4 tours à marcher vers le bulbe pendant que Tezcatlioca le frappait.

## Correction
Invocations ignorées tant qu'un poireau adverse est vivant. `analyze_fight.py` calcule maintenant la
distance au poireau adverse le plus proche même avec plusieurs entités.

## À noter
- Avec force 345, chaque coup adverse fait 130–180 : Solidification + Bouclier aurait été rentable dès le T3.
- Fréquence 150 contre 140 : il joue en premier.
