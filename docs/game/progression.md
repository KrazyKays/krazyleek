# Progression : ce qui change en montant de niveau

> Données : `docs/data/` + encyclopédie, relevé du 2026-11-26. Dégâts estimés pour force 220 (× 3,2).

## 1. Capital : les prix montent
- +5 capital par niveau, **+50 aux niveaux 100, 200, 300** (+100 au 301).
- Force/sagesse/agilité/résistance : 2 pts par capital jusqu'à +200, **1:1 jusqu'à +400**, puis 1 pt pour 2, puis pour 3.
- Vie : 4 PV/capital jusqu'à +1 000, puis 3, puis 2.
- PT : 30, 35, 40… (+5 par point) ; PM : 20, 40, 60… (+20) ; cœurs / RAM : 20, 30, 40… (+10).
- Conséquence : il faut **équilibrer** (aucune stat ne reste rentable longtemps). Recalculer le gain par
  capital à chaque palier (`build-recommendation.md`).
- 20 potions de restat gratuites : un changement de style (ex. passer magie/poison) est possible.

## 2. Armes et puces à venir (marché)
| Niv | Objet | PT | Portée | Intérêt | Prix |
|---|---|---|---|---|---|
| 38 | Laser (arme) | 6 | 2–9 ligne | ≈ 163 dégâts, 27/PT, 2 tirs | 12 120 |
| 40 | Solidification | 6 | 0–3 | +180–200 résistance 3 tours (boucliers × 3) | 24 400 |
| 42 | Venin | 4 | 1–10 | poison (ignore les boucliers) — utile avec de la magie | 66 600 |
| 48 | Bulbe chétif | 6 | — | 1ʳᵉ invocation : demande du code dédié | 42 420 |
| **50** | **Stalactite** | 6 | 2–7 | ≈ 210 dégâts, **35/PT** (recharge 3) | 54 500 |
| **60** | **Libération** | 5 | 0–6 | retire les buffs/boucliers adverses : contre les Domingo | 90 000 |
| 65 | Tranquillisant | 3 | 1–8 | vol de PT (avec magie) | 46 945 |
| 74 | Armure | 6 | 0–4 | bouclier absolu 25, 4 tours | 85 500 |
| 85 | Destructeur (arme) | 6 | 1–6 | ≈ 160 + vol de force | 45 320 |
| 100 | Iceberg | 7 | 3–5 | ≈ 275 dégâts | 87 330 |

Les prix grimpent vite : garder des habs, revendre l'équipement remplacé.

## 3. Composants (8 emplacements)
| Niv | Composant | Apport |
|---|---|---|
| 33 | CD | +40 sagesse |
| 37 | Plaque de fer | +50 PV, +40 résistance |
| 41 | Noyau XN.a-56 | +4 cœurs |
| 47 | **Batterie** | +10 résistance, +10 fréquence, **+1 PT** |
| 49 | Carte mère | +40 PV, +20 science, +10 fréquence, +2 cœurs, +2 RAM |
| 58 | Orange | +25 sagesse, +25 résistance, +20 fréquence |
Les composants s'améliorent aussi (« Component upgrades »). Ils ne comptent pas dans le coût en capital.

## 4. Adversaires : les styles à prévoir dans l'IA
| Style | Danger | Parade / code à prévoir |
|---|---|---|
| Soigneurs + boucliers (type Domingo) | combats qui s'éternisent, nuls | dégâts en rafale, Libération (60), ne pas laisser de tours vides |
| Poison / magie | ignore nos boucliers | soins, antidote ; ne pas surévaluer nos boucliers |
| Renvoi de dégâts (agilité) | chaque coup nous blesse | préférer peu de gros coups (rocher, éclair) aux multi-coups (mitraillette, étincelle) |
| Invocateurs (bulbes) | plusieurs cibles | ciblage : viser le poireau, ignorer les bulbes sauf s'ils bloquent |
| Kiteurs à 4+ PM | frappent en premier | 4ᵉ PM, ne pas entrer dans leur portée sans pouvoir frapper |
| Vol de PT/PM (entraves) | tours amputés | l'IA relit `getTP()`/`getMP()` à chaque tour : déjà géré |

## 5. Opérations et code
- 1 cœur = 1 M d'opérations/tour. L'IA actuelle : ~150–300 k. Marge confortable jusqu'à ce qu'on
  ajoute de la simulation (anticiper le tour adverse) : alors prendre des cœurs (composant niv. 41).
- L'IA est générique pour les dégâts, soins et boucliers. **Nouveau code nécessaire** pour :
  invocations, poison (dégâts sur la durée), entraves, téléportation/saut, Libération.

## 6. Autres modes
- Combats éleveur (4 contre 4) dès qu'on a plusieurs poireaux, équipe (6 contre 6 + tourelle),
  tournois, battle royale (jusqu'à 20 poireaux) : ciblage multi-ennemis et zones d'effet deviennent importants.
- Le talent monte avec les victoires → adversaires de plus en plus optimisés : l'IA fait la différence.

## 7. Améliorer un composant (encyclopédie « Component upgrades » / « Améliorations »)
1. **Détruire** des composants inutiles (Inventaire → onglet Détruire) → on récupère des **altérations**
   (même catégorie que le composant : fruit / physique / électronique, et ses caractéristiques) + une
   partie des ingrédients.
2. **Améliorer** (onglet Améliorer) : une « recette » = 1 composant + jusqu'à 8 altérations.
   - **Dose** = somme des doses des altérations ; chaque composant a un **métabolisme** (dose idéale)
     inconnu, à deviner par essais (l'historique affiche la proximité en %). Le métabolisme est figé
     dès le premier essai sur cet exemplaire.
   - **Charge** = somme des charges ; plus elle est haute, plus le risque de **casse** est grand et plus
     la dose doit être précise. Casse = perte aléatoire de caractéristiques (mais charge négative ajoutée,
     ce qui facilite les essais suivants).
   - Caractéristique **exceptionnelle** (non native) : une même stat exceptionnelle ne peut apparaître
     qu'une fois sur l'ensemble des composants équipés.
3. **Stratégie sûre** : on ne peut pas équiper deux fois le même composant, donc **crafter un 2ᵉ exemplaire,
   l'améliorer, et ne l'équiper qu'en cas de réussite**. Ne jamais tenter sur l'exemplaire équipé (une casse
   de la RAM ferait perdre des emplacements de puces).
   - RAM (recette : 1 lierre, 4 écrous, 4 briques) : chaque point de RAM = 1 puce de plus → **prioritaire**.
     Altérations RAM : détruire des RAM en surplus.
   - Ventilateur (9 branches, 1 plaque de métal, 2 écrous) : fréquence ; moins prioritaire (déjà 140).
