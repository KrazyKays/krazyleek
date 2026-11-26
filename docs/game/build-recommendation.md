# Config recommandée — krazyKlick (force 220, 10 PT, 3 PM)

> Calculs : dégâts moyens de base × (1 + force/100) = × 3,2 (formule confirmée par l'encyclopédie),
> d'après `docs/data/` (API officielle). 2 emplacements d'armes, 6 de puces (RAM 6).

## Tout ce qui est accessible au niveau ≤ 30 (dégâts par PT)

| Objet | Niv | Prix (habs) | PT | Portée | Lancer | Dégâts moy. | **Dégâts/PT** | Note |
|---|---|---|---|---|---|---|---|---|
| Éclair (`CHIP_FLASH`) | 24 | 4 890 | 3 | 1–10 | ligne | 107 | **35,7** | recharge 1, zone |
| Mitraillette (`WEAPON_MACHINE_GUN`) | 8 | 3 080 | 4 | 1–6 | ligne | 120 | **30,0** | 3 tirs/tour max |
| Caillou (`CHIP_PEBBLE`) ✔ | 4 | possédé | 2 | 0–5 | cercle | 58 | **28,8** | recharge 1, très aléatoire |
| Épée large (`WEAPON_BROADSWORD`) | 30 | 9 950 | 5 | 1 | cercle | 128 | 25,6 | corps à corps, +40 force |
| Rocher (`CHIP_ROCK`) | 13 | 7 400 | 5 | 2–6 | cercle | 123 | 24,6 | recharge 1 |
| Fusil à pompe (`WEAPON_SHOTGUN`) | 16 | 6 800 | 5 | 1–5 | ligne | 122 | 24,3 | |
| Flamme (`CHIP_FLAME`) | 29 | 5 560 | 4 | 2–7 | cercle | 96 | 24,0 | pas de recharge, 3/tour |
| Neutrino (`WEAPON_NEUTRINO`) | 12 | 8 250 | 4 | 2–6 | diagonale | 88 | 22,0 | + vulnérabilité |
| Magnum (`WEAPON_MAGNUM`) | 27 | 7 510 | 5 | 1–8 | cercle | 104 | 20,8 | |
| Pistolet ✔ | 1 | possédé | 3 | 1–7 | cercle | 56 | 18,7 | |
| Glace (`CHIP_ICE`) | 9 | 1 830 | 4 | 0–8 | cercle | 58 | 14,4 | |
| Étincelle ✔ | 19 | possédé | 3 | 0–10 | cercle, **sans LdV** | 38 | 12,8 | |
| Choc (`CHIP_SHOCK`) | 2 | 1 780 | 2 | 0–6 | cercle | 26 | 12,8 | |

Les puces piquant, capsaïcine, sucre, pop-corn, apocalypse… ne sont pas en vente (hors marché).

## Recommandation

**Armes**
1. **Mitraillette** (3 080) : meilleure arme accessible par PT. Limite : tir en ligne uniquement.
2. **Pistolet** (déjà possédé) en 2ᵉ arme si tu as 2 emplacements : tir en cercle quand on n'est pas aligné.

**Puces (6)**
| Garder / acheter | Pourquoi |
|---|---|
| **Éclair** (achat 4 890) | Meilleurs dégâts/PT, portée 10 |
| **Flamme** (achat 5 560) | Attaque en cercle sans recharge : couvre les tours où on n'est pas aligné |
| Caillou ✔ | Très rentable pour 2 PT |
| Protéines ✔ | +28 % de dégâts pendant 2 tours |
| Motivation ✔ | +2 PT pendant 3 tours, idéale pendant l'approche |
| Bandage ✔ | Utilise les 2 PT qui restent souvent en fin de tour |

**À retirer** : casque (bouclier 15 = ~10 PV sauvés par PT, faible) et étincelle (12,8 dégâts/PT).
Budget total : **13 530 habs** (moins la revente du casque et de l'étincelle).
Ordre d'achat si budget limité : mitraillette → éclair → flamme.

**Capital** : voir la section « Répartition du capital » plus bas.

## Gain attendu sur un tour à 10 PT

| Situation | Actuel | Recommandé |
|---|---|---|
| Aligné, à ≤ 6 cases | caillou + 2 pistolets ≈ 170 | éclair + caillou + mitraillette ≈ **285** |
| Tour où éclair/caillou rechargent | 3 pistolets ≈ 168 | 2 mitraillettes + bandage ≈ **240** |
| Pas aligné, 2–7 cases | caillou + 2 pistolets ≈ 170 | 2 flammes + caillou ≈ **250** |

Soit environ **+45 à +70 % de dégâts par tour**.

## Mise à jour niveau 33 : 10 emplacements de puces (composant RAM)

Les 4 nouveaux emplacements, par ordre de priorité :

| Puce | Prix | Rôle |
|---|---|---|
| **Casque** (déjà acheté) | 2 200 | Bouclier absolu 15 **par coup** pendant 2 tours. Contre 4 étincelles/tour : −60 dégâts/tour, soit ~120 dégâts évités pour 3 PT (40/PT, mieux que n'importe quelle attaque). L'IA le lance quand l'adversaire frappe souvent. |
| **Rocher** | 7 400 | 24,6 dégâts/PT en cercle (portée 2–6) : combo 10 PT éclair + rocher + caillou ≈ 288 dégâts sans besoin d'alignement pour le rocher. |
| **Étincelle** (déjà achetée) | 2 910 | Seule attaque sans ligne de vue : touche un adversaire caché derrière un mur. |
| **Bottes en cuir** | 3 800 | +2 PM pendant 2 tours : l'IA les lance quand aucune attaque n'est possible, pour atteindre une position de tir. |

Alternative au 4ᵉ : **Soin** (3 710, soin 38–46, mieux avec de la sagesse).

**Composant à crafter : CD** (niveau 33, +40 sagesse) : soins × 1,4 et vol de vie = 4 % des
dégâts infligés (~10 PV/tour). Il reste 4 emplacements de composants.

**Fréquence 140** (ventilateur) : contre un adversaire à 100, ~72 % de chances de jouer en premier.

## Répartition du capital

Situation (déduite) : 195 capital au niveau 30, 5 non dépensés. Force 220 = 200 investis
(100 capital, au ratio 2:1) + 20 du ressort ; vie 647 = 187 de base + 100 de la pomme + 360 investis
(90 capital). La force est donc au bout du ratio avantageux : **chaque point coûte maintenant 1 capital**.

Gain par point de capital (objectif : dégâts × survie) :

| Investissement | Effet | Gain / capital |
|---|---|---|
| Vie | +4 PV sur 647 | **+0,62 %** de survie |
| Force | +1 sur 320 (100 + force) | +0,31 % de dégâts |
| 11ᵉ PT (30 capital) | permet mitraillette ×2 + éclair (11 PT) | ≈ +21 % de dégâts → **+0,7 %** |
| 4ᵉ PM (20 capital) | plus d'options pour s'aligner / se cacher / jouer avant | non chiffré, fort au bas niveau |
| 2ᵉ cœur | inutile : l'IA consomme ~40 000 opérations sur 1 000 000 | 0 |
| 7ᵉ RAM (20 capital) | 1 puce de plus (ex. garder le casque) | faible pour l'instant |

**Plan conseillé** (210 capital au niveau 33)
1. **11ᵉ PT** (30 capital) dès que possible : au niveau 35 si 20 points sont en réserve au niveau 33.
2. Ensuite **4ᵉ PM** (20 capital, 4 niveaux).
3. Ensuite **vie** en continu : 2× plus rentable que la force jusqu'à environ 1 300 PV
   (point où +4 PV et +1 force rapportent autant).
4. Force à nouveau quand la vie dépasse ~1 300, ou si la config change.

Pas besoin de restat : la répartition actuelle est déjà équilibrée (simuler 30 capital de vie
convertis en 1 PT donne ≈ −18 % de PV pour +21 % de dégâts, quasi neutre).
