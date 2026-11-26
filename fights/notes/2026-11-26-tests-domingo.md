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
