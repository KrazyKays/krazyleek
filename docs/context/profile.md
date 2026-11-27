# Profil joueur

> Source de vérité pour adapter les IA. Mettre à jour à chaque changement de build.
> Dernière mise à jour : 2026-11-26.

## Éleveur
- Talent éleveur : 100
- Mode joué : **solo** (prioritaire), quelques tournois sans enjeu
- Langage des IA : **LeekScript v4** (migration depuis Python le 2026-11-26)

## Poireaux

### krazyKlick — niveau 50

Stats au niveau 47 (combat 54984587) :

| Vie | Force | Sagesse | Agilité | Résistance | Science | Magie | Fréquence | PT | PM | Cœurs | RAM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 887 | 220 | 0 | 40 | 0 | 0 | 0 | **140** | **11** | **4** | 1 | **10** |

- Capital : 295 au total au niveau 50 ; tout en vie. Habs : largement assez pour la Stalactite
- Emplacements : **2 armes**, **10 puces** (RAM 10), jusqu'à 8 composants
- Armes : laser, mitraillette
- Puces (10/10) : éclair, flamme, caillou, rocher, protéines, motivation, étincelle, bouclier, Solidification, **bulbe chétif** (casque retiré au niv. 48 ; bandage au niv. 46)
- Composants (4/8) : ressort (+20 force, +40 agilité), pomme (+100 PV), RAM (+4 RAM), ventilateur (+40 fréquence)
  Recettes possédées non craftées : CD (manque 3 jus de poireau), noyau XN.a-56 (+4 cœurs),
  **Morus** (+60 PV, +20 sagesse, +40 magie ; 4 feuilles, 2 fleurs, 2 jus de poireau, 4 chairs d'aubergine)
  Recette obtenue, ressources manquantes : **plaque de fer** (30 rochers, 50 briques, 20 cailloux, 40 écrous)
  Pas encore obtenues : batterie, carte mère (recettes aléatoires en fin de combat)
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
- **Kiteurs rapides niv. 50** (5–6 PM + bottes, propulseur, Stalactite) : Portemurmure 54979684, Fabistan 54979702.
  Ils frappent puis sortent de notre portée (4 PM) : 0 à 233 dégâts infligés.
- (à compléter avec des liens de combats)
