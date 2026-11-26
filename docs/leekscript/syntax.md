# LeekScript v4 — syntaxe essentielle

> Référence officielle : https://leekwars.com/help/documentation (à consulter en cas de doute).
> Les points marqués *(à vérifier)* n'ont pas encore été confirmés en jeu.

## Exécution
- L'IA est exécutée **une fois par tour** du poireau, de haut en bas.
- Les variables `var` locales au fichier sont réinitialisées à chaque tour.
- Les variables `global` sont initialisées une seule fois (premier tour) et **persistent** entre les tours.

```leekscript
global turnCount = 0;   // initialisé au 1er tour seulement
turnCount++;
var me = getEntity();   // recalculé à chaque tour
```

## Variables et types
```leekscript
var a = 12;               // type dynamique
integer b = 3;            // typage optionnel (v4)
real c = 1.5;
string s = "texte";
boolean ok = true;
Array<integer> list = [1, 2, 3];
Map<string, integer> m = ["pv": 100, "pm": 3];
var n = null;
```

## Fonctions
```leekscript
function distanceTo(entity) {
    return getCellDistance(getCell(), getCell(entity));
}

// Fonction anonyme / lambda
var double = function(x) { return x * 2; };
var triple = x -> x * 3;          // (à vérifier : syntaxe flèche v4)
```

## Contrôle de flux
```leekscript
if (x > 0) { ... } else if (x == 0) { ... } else { ... }
while (cond) { ... }
for (var i = 0; i < 10; i++) { ... }
for (var value in list) { ... }
for (var key : var value in map) { ... }
```

## Tableaux et maps (fonctions utiles)
`count(arr)`, `push(arr, v)`, `remove(arr, i)`, `inArray(arr, v)`, `search(arr, v)`,
`arraySort(arr, cmp)`, `arrayFilter(arr, f)`, `arrayMap(arr, f)`, `arrayMin`, `arrayMax`,
`mapKeys(map)`, `mapValues(map)`, `mapContainsKey(map, k)`.

## Classes (v2+)
```leekscript
class Target {
    entity
    score
    constructor(entity, score) {
        this.entity = entity
        this.score = score
    }
}
var t = new Target(enemy, 42);
```

## Inclusion de modules
```leekscript
include("lib/movement");   // nom de l'IA telle qu'elle existe sur Leek Wars
```
- *(à vérifier)* : résolution des chemins relatifs dans les dossiers de l'éditeur.
- Un module inclus est exécuté à l'endroit de l'`include` ; y déclarer surtout des fonctions.

## Debug
- `debug(valeur)` : affiche dans le log du combat.
- `debugW` / `debugE` : warning / erreur.
- `mark(cell, color)` et `markText(cell, texte)` : marquer des cases dans le replay.
- `getOperations()` : opérations consommées depuis le début du tour.
