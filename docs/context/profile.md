# Profil joueur

> Source de vérité pour adapter les IA. Mettre à jour à chaque changement de build.
> Dernière mise à jour : 2026-11-26.

## Éleveur
- Talent éleveur : 100
- Mode joué : **solo** (prioritaire), quelques tournois sans enjeu
- Langage des IA : **LeekScript v4** (migration depuis Python le 2026-11-26)

## Poireaux

### krazyKlick — niveau 35

Stats au niveau 32 (combat 54965116) + RAM et ventilateur (niveau 33) + 11ᵉ PT (niveau 35) :

| Vie | Force | Sagesse | Agilité | Résistance | Science | Magie | Fréquence | PT | PM | Cœurs | RAM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 662 | 220 | 0 | 40 | 0 | 0 | 0 | **140** | **11** | 3 | 1 | **10** |

- Capital : 220 au total au niveau 35 ; non dépensé : 0 (estimé, après achat du 11ᵉ PT)
- Emplacements : **2 armes**, **10 puces** (RAM 10), jusqu'à 8 composants
- Armes : mitraillette, pistolet
- Puces (6/10) : éclair, flamme, caillou, protéines, motivation, bandage
- Composants : ressort (+20 force, +40 agilité), pomme (+100 PV), RAM (+4 RAM), ventilateur (+40 fréquence)
- IA utilisée : [`ai/main.leek`](../../ai/main.leek) (planificateur générique)
  Ancienne IA Python : [`ai/legacy/krazyklick_v0.py`](../../ai/legacy/krazyklick_v0.py)
- Config cible : voir [`docs/game/build-recommendation.md`](../game/build-recommendation.md)

## Objectifs
- Court terme : progresser en solo.
- Long terme : à définir.

## Adversaires problématiques
- **Coffres** : ont tué krazyKlick plusieurs fois en solo → l'IA ne les touche plus (voir `ai/lib/threat.leek`).
- **Kiteur étincelle derrière un mur** (Prunaux, combat 54965116) : bug d'approche corrigé ;
  le casque est la parade (bouclier par coup).
- (à compléter avec des liens de combats)
