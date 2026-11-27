# Mécaniques de jeu

> Source : encyclopédie officielle (API `encyclopedia/get/en/<page>`), relevé du 2026-11-26.

## Ressources par tour
- **PT** : payent armes, puces, changement d'arme (1 PT).
- **PM** : 1 PM = 1 case. Rechargés à chaque tour.
- **Cœurs** : +1 million d'opérations par tour chacun (1 cœur = 1 M d'opérations).
- **RAM** : 1 point = 1 emplacement de puce (+ mémoire pour l'IA).

## Formules (confirmées)
| Stat | Formule |
|---|---|
| Force | `dégâts = base × (1 + force/100)` |
| Sagesse | `soin = base × (1 + sagesse/100)` ; vol de vie = `dégâts infligés × sagesse/1000` |
| Résistance | `bouclier = base × (1 + résistance/100)` (fixé au lancement) |
| Agilité | chance de critique = `agilité/1000` ; critique = × `CRITICAL_FACTOR` (1,3) ; renvoi de dégâts × (1 + agilité/100) |
| Fréquence | ordre de jeu : P(jouer en premier) = `1 − 1/(1 + 10^(écart/100))` |
| Dégâts reçus | `dégâts × (1 − bouclier relatif/100) − bouclier absolu` (poison, renvoi et nova ignorent les boucliers) |

## Coût du capital
Capital total au niveau N (N < 100) : `50 + 5 × (N − 1)` → **195 au niveau 30**, +5 par niveau.

| Stat | Coût |
|---|---|
| Vie | 1 capital = 4 PV (jusqu'à +1 000), puis 3, puis 2 |
| Force, sagesse, agilité, résistance | 1 capital = 2 pts (jusqu'à +200), puis 1:1 (jusqu'à +400), puis 1:2, puis 1:3 |
| Science, magie | *(supposé identique, non relevé)* |
| Fréquence | 1:1 |
| PT | 30 pour le 11ᵉ, +5 par point ensuite (max 100) |
| PM | 20 pour le 4ᵉ, +20 par point ensuite (max 180) |
| Cœurs | 20 pour le 2ᵉ, +10 ensuite |
| RAM | 20 pour le 7ᵉ point, +10 ensuite |

Vie de base : `100 + 3 × (niveau − 1)` = 187 au niveau 30.
Potions de restat : stock limité (**3 restantes** au 2026-11-27) → toute redistribution du capital est précieuse.

## Combats quotidiens (potager)
- **50 combats/jour communs à tous les poireaux** (+50 achetables en habs), à répartir entre :
  solo (1 c 1), éleveur (4 c 4), arènes (10 à 20 entités), boss (8 c 8).
- Combats **équipe (6 c 6)** : tickets séparés, 10 par jour.
- Nombre de poireaux : un 3ᵉ poireau exige d'avoir un poireau niveau 100.

## Coffres (`ENTITY_CHEST`)
- Apparition : 1 combat sur 20 (jardin, tournois, BR ; jamais en combat de test).
- **Ne fait rien tant qu'il a 100 % de ses PV.** Une fois touché : se soigne, se protège
  (< 75 % PV), puis attaque **une entité au hasard à sa portée**.
- N'appartient à aucune équipe. Le tuer rapporte ressources et puissance au tueur.

| Type | PV | PT | Force | Sagesse | Résistance | Puces | Récompense |
|---|---|---|---|---|---|---|---|
| Bois | 2 000 | 20 | 500 | 200 | 0 | soin, rocher | 30 000 habs |
| Fer | 5 000 | 20 | 1 000 | 500 | 500 | rocher, rémission, éboulement, bouclier | 300 000 habs |
| Diamant | 20 000 | 20 | 2 000 | 1 000 | 1 000 | rocher, rémission, … | 3 500 000 habs |

Rocher d'un coffre en bois ≈ 38,5 × 6 = **231 dégâts** (portée 2–6) ; éboulement d'un coffre en fer
≈ 54 × 11 ≈ **590 dégâts** en zone (portée 5–7). Un coffre réveillé tue krazyKlick en 1 à 3 tours.

## Carte
- Grille en losange, obstacles ; distances de Manhattan.
- `MAX_TURNS` = 64.
