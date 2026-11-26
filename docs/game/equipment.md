# Équipement de krazyKlick — valeurs officielles

> Source : API Leek Wars (`docs/data/chips.json`, `docs/data/weapons.json`), relevé du 2026-11-26.
> Rafraîchir avec `python3 tools/fetch_api_data.py`.
> Lecture des effets : valeur = `value1` à `value1 + value2` (tirage aléatoire).

## Valeurs brutes

| Objet | Constante | PT | Portée | Ligne de vue | Recharge | Max/tour | Effet de base | Durée |
|---|---|---|---|---|---|---|---|---|
| Pistolet | `WEAPON_PISTOL` | 3 | 1–7 | oui | — | 4 | Dégâts 15–20 | — |
| Caillou | `CHIP_PEBBLE` | 2 | 0–5 | oui | 1 | — | Dégâts 2–34 | — |
| Étincelle | `CHIP_SPARK` | 3 | 0–10 | **non** | 0 | 5 | Dégâts 8–16 | — |
| Bandage | `CHIP_BANDAGE` | 2 | 0–6 | oui | 1 | — | Soin 23–28 | — |
| Casque | `CHIP_HELMET` | 3 | 0–4 | oui | 3 | — | Bouclier absolu 15 | 2 tours |
| Protéines | `CHIP_PROTEIN` | 3 | 0–4 | oui | 3 | — | Force +80–100 | 2 tours |
| Motivation | `CHIP_MOTIVATION` | 4 | 0–5 | oui | 6 | — | PT +2 | 3 tours |

Toutes ces puces se lancent en cercle (`LAUNCH_TYPE_CIRCLE`) sur une seule case.
Les buffs (casque, protéines, motivation) ciblent le lanceur.

## Avec le build actuel (force 220, sagesse 0, résistance 0, science 0)

Hypothèse (voir `mechanics.md`) : dégâts × (1 + force/100) = **× 3,2**.

| Action | Dégâts / effet estimé | Moyenne | Moyenne par PT |
|---|---|---|---|
| Caillou | 6–109 | 58 | **28,8** |
| Pistolet | 48–64 | 56 | 18,7 |
| Étincelle | 26–51 | 38 | 12,8 |
| Bandage | soin 23–28 (sagesse 0) | 25,5 | 12,8 |
| Protéines | force +80–100 → × ~4,1 au lieu de × 3,2 | +28 % de dégâts | — |

## Enseignements
- **Le caillou est l'attaque la plus rentable par PT** (mais très aléatoire et une fois sur deux à cause de la recharge).
- **L'étincelle ne demande pas de ligne de vue** : on peut tirer de derrière un obstacle jusqu'à 10 cases.
  C'est la base d'une stratégie de harcèlement à couvert.
- Avec 10 PT : 3 tirs de pistolet maximum (9 PT) ; avec motivation (12 PT) : 4 tirs (le maximum par tour).
- Protéines : rentable si on attaque sur les 2 tours qu'elle dure (~+50 dégâts/tour pour 3 PT).
- Motivation : 4 PT pour +2 PT × 3 tours = +2 PT net, intéressante au 1er tour quand l'ennemi est encore loin.
- Le seuil de soin de 28 PV perdus correspond exactement au soin max du bandage : bon réglage.
