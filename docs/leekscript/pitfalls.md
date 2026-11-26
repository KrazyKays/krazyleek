# Pièges connus

> À enrichir à chaque bug découvert : symptôme → cause → correctif.

1. **Limite d'opérations** : dépasser la limite du tour stoppe l'IA net (le poireau ne joue plus
   ses actions restantes). `getPathLength` dans une boucle sur toutes les cases est la cause n°1.
   → Pré-calculer, mettre en cache dans une `global`, réduire l'espace de recherche.
2. **`setWeapon` coûte 1 PT** : ne changer d'arme que si nécessaire, et en tenir compte dans le budget de PT.
3. **Distance ≠ chemin** : `getCellDistance` ignore les obstacles ; une cible « à portée » peut être
   hors de vue. Toujours vérifier `lineOfSight` ou `canUseWeapon`.
4. **Ordre déplacement / attaque** : se déplacer consomme des PM, pas des PT. Penser
   « attaquer puis fuir » (kite) aussi bien que « avancer puis attaquer ».
5. **Cible morte en cours de tour** : après un kill, `getNearestEnemy()` change ; recalculer la cible
   avant de continuer à tirer.
6. **`global` initialisée une seule fois** : une `global` avec une valeur calculée (ex. `getCell()`)
   garde la valeur du premier tour.
7. **`include` sans extension** : `include("lib/utils")` → fichier introuvable.
   Il faut écrire `include("lib/utils.leek")`.
8. **Réveiller un coffre** : un coffre à 100 % de PV est inoffensif ; une seule touche (y compris
   une zone qui déborde, ex. éclair) le réveille et il frappe très fort. Ne jamais l'inclure dans
   une zone d'effet ; ne l'attaquer que pour l'achever (`ai/lib/threat.leek`).
9. **Coût en opérations mesuré** : planificateur ≈ 40 000 opérations/tour (limite 1 M avec 1 cœur).
10. **Minimum local derrière un mur** : choisir sa case par distance de Manhattan bloque le poireau
    contre un obstacle. Utiliser le vrai chemin (`moveToward`, `moveTowardCells`,
    `getCellsToUseWeapon/Chip`). Ne jamais « reculer » un tour où on n'a pas attaqué.
    (Combat 54965116, `fights/notes/2026-11-26-defaite-etincelle-derriere-mur.md`.)
