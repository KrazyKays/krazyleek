# Tests contre Domingo (bot de test) — niveau 35

Combats 54966254, 54966311, 54966444 (analyse : `python3 tools/analyze_fight.py <id>`).
Résultat : **3 victoires** (tours 5, 11, 9). Dégâts infligés / subis : 478/86, 798/545, 565/217.
Opérations : ~150 000 à 200 000 par tour (limite 1 M).

## Ce qui marche
- Approche par le vrai chemin : plus de blocage derrière les murs.
- Combos au contact : protéines + éclair + rocher (300 dégâts), 2 flammes + éclair, kills propres.
- Étincelle utilisée hors ligne de vue (T8 et T10 du combat 54966311).

## Gaspillages corrigés
- Motivation, bouclier et casque lancés au tour 1 à 10–28 cases : expirés avant le contact.
- Boucliers relancés aux tours 4–5 encore loin → en recharge au tour 8 (211 dégâts subis sans bouclier).
→ Motivation seulement si le combat commence d'ici un tour (`combatSoon`), boucliers seulement
  si l'adversaire peut nous frapper à son prochain tour (`enemyCanReach`), évalués après le repli.

## Normal
- Tours d'approche sans action (aucune cible à portée) : 11–13 PT non utilisés, inévitable.

## Combats 54966684 (victoire T11) et 54966751 (nul à 64 tours)
- 54966751 : Domingo campe dans un coin derrière des murs et se soigne ~60 PV/tour (soin + boucliers).
  Nous : étincelle ×3 (~100) puis repli de 3 cases ; tour suivant : retour sans attaque.
  → ~50 dégâts/tour en moyenne < soins adverses → nul (1 801 infligés / 220 subis).
- Même va-et-vient dans 54966684 (cases 431 ↔ 450), gagné quand même.
- Correction : `retreatFrom` ne fuit que vers une case hors de portée de l'adversaire ET d'où l'on
  peut encore attaquer au tour suivant ; sinon on reste à portée (repli seulement derrière un mur proche).
