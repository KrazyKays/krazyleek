# Profil joueur

> Source de vérité pour adapter les IA. Mettre à jour à chaque changement de build.
> Dernière mise à jour : 2026-11-26.

## Éleveur
- Talent éleveur : 100
- Mode joué : **solo** (prioritaire), quelques tournois sans enjeu
- Langage des IA : **LeekScript v4** (migration depuis Python le 2026-11-26)

## Poireaux

### krazyKlick — niveau 40

Stats au niveau 40 (combat 54977259) :

| Vie | Force | Sagesse | Agilité | Résistance | Science | Magie | Fréquence | PT | PM | Cœurs | RAM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 677 | 220 | 0 | 40 | 0 | 0 | 0 | **140** | **11** | **4** | 1 | **10** |

- Capital : 245 au total au niveau 40 (4ᵉ PM acheté) ; non dépensé : à confirmer
- Emplacements : **2 armes**, **10 puces** (RAM 10), jusqu'à 8 composants
- Armes : mitraillette, pistolet
- Puces (10/10, supposé d'après les recommandations) : éclair, flamme, caillou, rocher, étincelle, protéines,
  motivation, bandage, casque, **bouclier** (remplace les bottes en cuir au niveau 35)
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
- **Tanks Solidification + Bouclier** (BigLittlePhi niv. 43, combat 54977259) : bouclier 63/coup pendant 3 tours ;
  fusil à pompe adverse qui annule nos boucliers. Parade future : Libération (niv. 60).
- (à compléter avec des liens de combats)
