# API Leek Wars — fonctions courantes

> Liste de travail, non exhaustive. **Ne pas utiliser une fonction absente de cette liste sans la vérifier**
> dans la doc officielle (https://leekwars.com/help/documentation), puis l'ajouter ici.
> Sans argument `entity`, la plupart des fonctions s'appliquent au poireau courant.

## Entités
| Fonction | Rôle |
|---|---|
| `getEntity()` | Id de l'entité courante (mon poireau) |
| `getLeek()` | **Dépréciée** → `getEntity()` |
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
| `canUseWeapon([weapon,] entity)` | Faisabilité (arme optionnelle) |
| `getWeaponCost(w)`, `getWeaponMinRange(w)`, `getWeaponMaxRange(w)` | Caractéristiques |
| `getWeaponEffects(w)` | Effets (dégâts min/max…) |

## Puces
| Fonction | Rôle |
|---|---|
| `getChips(e)` | Puces équipées |
| `useChip(chip, target)` / `useChipOnCell(chip, cell)` | Utiliser → code retour |
| `canUseChip(chip, target)` | Faisabilité |
| `getCooldown(chip[, entity])` | Recharge restante ; `getChipCooldown(chip)` = recharge de base |
| `getChipCost(chip)`, `getChipMinRange(chip)`, `getChipMaxRange(chip)` | Caractéristiques |
| `getChipEffects(chip)` | Effets |
| `summon(chip, cell, aiFunction)` | Invocation (bulbe) |

## Codes retour d'utilisation
`USE_SUCCESS` (1), `USE_CRITICAL` (2, coup critique), `USE_FAILED` (0), `USE_INVALID_TARGET` (-1),
`USE_NOT_ENOUGH_TP` (-2), `USE_INVALID_COOLDOWN` (-3), `USE_INVALID_POSITION` (-4),
`USE_TOO_MANY_SUMMONS` (-5), `USE_MAX_USES` (-7), `USE_INVALID_STATE` (-8). Réussite = valeur > 0.

## Tour et divers
| Fonction | Rôle |
|---|---|
| `getTurn()` | Numéro du tour |
| `getOperations()` | Opérations consommées |
| `debug(x)`, `mark(c, color)`, `markText(c, txt)` | Debug |
| `say(msg)` | Bulle de dialogue (coûte 1 PT) |

## Constantes vérifiées (API officielle)
- Équipement : `WEAPON_PISTOL`, `CHIP_PEBBLE`, `CHIP_SPARK`, `CHIP_BANDAGE`, `CHIP_HELMET`,
  `CHIP_PROTEIN`, `CHIP_MOTIVATION` — valeurs détaillées dans `docs/game/equipment.md`.
- Entités : `getType(e)` → `ENTITY_LEEK`, `ENTITY_BULB`, `ENTITY_TURRET`, `ENTITY_CHEST`, `ENTITY_MOB`, `ENTITY_PLANT`.
- `OPERATIONS_LIMIT` = 20 000 000.

## Référence complète
La liste exhaustive (fonctions, arguments optionnels, coût en opérations, dépréciations) est dans
`docs/data/functions.json` et `docs/data/constants.json`. Vérifier le code avec :
`python3 tools/check_api.py`.
