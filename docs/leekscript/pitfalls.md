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
11. **Cibler une invocation** : un bulbe a peu de PV, donc un ciblage « PV les plus bas » le choisit.
    Toujours exclure `isSummon(e)` tant qu'un poireau adverse est vivant (combat 54977534).
12. **Plan sans dégâts jeté** : filtrer les cases sur « dégâts > 0 » élimine les plans purement défensifs
    (Solidification + Bouclier) que le planificateur a pourtant jugés meilleurs → « aucune attaque possible »
    et tour vide. Garder une case si elle a des dégâts OU des puces sur soi (combat 54977580, tours 4, 6, 8).
13. **Tirs amis** : les effets de dégâts ciblent aussi les alliés (cibles 31). L'éclair (zone cercle 1)
    et surtout le **laser** (`AREA_LASER_LINE` : touche tout ce qui est aligné dans la direction du tir,
    jusqu'à la portée max) peuvent blesser un coéquipier. Vérifié par `wouldHitAlly` (lib/team.leek).
14. **Distance « à vol d'oiseau » pour se déplacer = boucle** : choisir sa case par distance de Manhattan
    vers des cases cibles fait tourner en rond autour des murs (combat 54979521 : 56 tours d'allers-retours).
    Toujours laisser le jeu calculer le chemin (`moveTowardCells`, `moveToward`) et garder un détecteur
    de boucle (`isStuck` dans lib/movement.leek).

## Outils
- `api/fight/get/<id>` répond **409 `fight_with_secret_trophy`** pour un combat qui contient un trophée secret :
  l'analyse automatique est impossible sans être connecté. Récupérer le JSON depuis le navigateur et le passer
  à `tools/analyze_fight.py <fichier.json>`.

## Tactique
- **Approche** : avancer jusqu'à « portée adverse + PM adverses » sans pouvoir tirer offre la première salve
  à l'adversaire (54991303). S'arrêter une case avant (`holdOutsideReach`).
