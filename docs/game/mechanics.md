# Mécaniques de jeu

> Formules à confirmer avec la doc officielle / l'encyclopédie (https://leekwars.com/encyclopedia).
> Tout ce qui est marqué *(à vérifier)* ne doit pas servir de base à une optimisation fine.

## Ressources par tour
- **PT** (points de tour) : payent armes, puces, changement d'arme.
- **PM** (points de mouvement) : 1 PM = 1 case.
- Les deux sont rechargés au début de chaque tour du poireau.

## Caractéristiques et effets
| Stat | Effet principal |
|---|---|
| Vie | PV max |
| Force | Augmente les dégâts : `dégâts ≈ base × (1 + force/100)` |
| Sagesse | Augmente les soins : `soin ≈ base × (1 + sagesse/100)` |
| Résistance | Augmente les boucliers donnés : `bouclier ≈ base × (1 + résistance/100)` |
| Agilité | Chance de critique et renvoi de dégâts *(détail à vérifier)* |
| Science | Augmente les boosts (buffs de stats) *(à vérifier)* |
| Magie | Augmente poisons et malus |
| Fréquence | Ordre de jeu (qui joue en premier) |

## Dégâts subis
`dégâts reçus ≈ dégâts × (1 − bouclier relatif/100) − bouclier absolu` *(ordre exact à vérifier)*

## Carte
- Grille en losange de 613 cases *(à vérifier selon le type de combat)*, avec obstacles.
- Distances de Manhattan ; portée des armes en ligne / en zone selon l'arme.
