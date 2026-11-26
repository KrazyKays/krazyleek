# API Leek Wars — fonctions courantes

> Liste de travail, non exhaustive. **Ne pas utiliser une fonction absente de cette liste sans la vérifier**
> dans la doc officielle (https://leekwars.com/help/documentation), puis l'ajouter ici.
> Sans argument `entity`, la plupart des fonctions s'appliquent au poireau courant.

## Entités
| Fonction | Rôle |
|---|---|
| `getEntity()` | Id de l'entité courante (mon poireau) |
| `getLeek()` | Id de mon poireau *(ancien nom, préférer getEntity)* |
| `getNearestEnemy()` | Ennemi le plus proche |
| `getEnemies()` / `getAliveEnemies()` | Ennemis (tous / vivants) |
| `getAllies()` / `getAliveAllies()` | Alliés |
| `isAlive(e)`, `isEnemy(e)`, `isAlly(e)`, `isSummon(e)` | Tests |
| `getName(e)`, `getLevel(e)` | Infos |

## Caractéristiques
| Fonction | Rôle |
|---|---|
| `getLife(e)`, `getTotalLife(e)` | PV actuels / max |
| `getTP(e)`, `getMP(e)` | PT / PM restants ce tour |
| `getStrength(e)`, `getAgility(e)`, `getWisdom(e)`, `getResistance(e)`, `getScience(e)`, `getMagic(e)` | Stats |
| `getAbsoluteShield(e)`, `getRelativeShield(e)` | Boucliers |
| `getEffects(e)` | Effets actifs (buffs, poisons…) |

## Carte et déplacements
| Fonction | Rôle |
|---|---|
| `getCell(e)` | Case de l'entité |
| `getCellX(c)`, `getCellY(c)`, `getCellFromXY(x, y)` | Coordonnées |
| `getCellDistance(c1, c2)` | Distance de Manhattan (sans obstacles) |
| `getPathLength(c1, c2)` | Longueur du chemin réel (obstacles) — coûteux |
| `lineOfSight(c1, c2)` | Ligne de vue entre deux cases |
| `isObstacle(c)`, `isEmptyCell(c)` | État d'une case |
| `moveToward(e)` / `moveToward(e, mp)` | Se rapprocher d'une entité |
| `moveTowardCell(c)` | Aller vers une case |
| `moveAwayFrom(e)` | S'éloigner d'une entité |

## Armes
| Fonction | Rôle |
|---|---|
| `getWeapon()` / `setWeapon(w)` | Arme en main / changer (coûte 1 PT) |
| `getWeapons(e)` | Armes équipées |
| `useWeapon(target)` | Tirer sur une entité → code retour |
| `useWeaponOnCell(cell)` | Tirer sur une case |
| `canUseWeapon(target)` / `canUseWeaponOnCell(w, from, to)` *(signature à vérifier)* | Faisabilité |
| `getWeaponCost(w)`, `getWeaponMinRange(w)`, `getWeaponMaxRange(w)` | Caractéristiques |
| `getWeaponEffects(w)` | Effets (dégâts min/max…) |

## Puces
| Fonction | Rôle |
|---|---|
| `getChips(e)` | Puces équipées |
| `useChip(chip, target)` / `useChipOnCell(chip, cell)` | Utiliser → code retour |
| `canUseChip(chip, target)` | Faisabilité |
| `getChipCooldown(chip)` / `getCooldown(chip)` *(nom à vérifier)* | Recharge restante |
| `getChipCost(chip)`, `getChipMinRange(chip)`, `getChipMaxRange(chip)` | Caractéristiques |
| `getChipEffects(chip)` | Effets |
| `summon(chip, cell, aiFunction)` | Invocation (bulbe) |

## Codes retour d'utilisation
`USE_SUCCESS`, `USE_FAILED`, `USE_NOT_ENOUGH_TP`, `USE_INVALID_TARGET`,
`USE_INVALID_POSITION`, `USE_INVALID_COOLDOWN` *(liste à vérifier)*.
Note : un coup critique renvoie `USE_CRITICAL` *(à vérifier)*.

## Tour et divers
| Fonction | Rôle |
|---|---|
| `getTurn()` | Numéro du tour |
| `getOperations()` | Opérations consommées |
| `debug(x)`, `mark(c, color)`, `markText(c, txt)` | Debug |
| `say(msg)` | Bulle de dialogue (coûte 1 PT) |

## Constantes utilisées par krazyKlick *(noms à vérifier en jeu)*
`WEAPON_PISTOL`, `CHIP_PEBBLE` (caillou), `CHIP_SPARK` (étincelle), `CHIP_BANDAGE`,
`CHIP_HELMET` (casque), `CHIP_PROTEIN` (protéines), `CHIP_MOTIVATION`.
`getType(e)` et `ENTITY_CHEST` (détection des coffres).

Coûts / portées / recharges : non relevés (leekwars.com inaccessible depuis l'environnement).
À compléter depuis l'encyclopédie du jeu.
