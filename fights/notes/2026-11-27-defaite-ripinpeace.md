# Défaite contre RipInPeace (niv. 50 !) — 54977555

- Lui : niveau **50** (nous 42), 587 PV, force 295, résistance 80, 11 PT, **5 PM** ; fusil à pompe + magnum,
  **stalactite**, Solidification, bouclier, casque, bulbe, soins ; 7 composants.
- Nous : 743 PV, laser + mitraillette, Solidification. Mort au tour 6 : 314 infligés / 798 subis.

## Déroulé
- T3 : nous motivation + Solidification + casque ; lui stalactite (275).
- T4 : bouclier + laser (20 seulement : son bouclier ≈ 74 + casque ≈ 55 par coup) + bandage.
- T5 : déplacement, bandage, **11 PT inutilisés** (pas de position d'attaque atteinte ; cause exacte → logs `[plan]`).
- T6 : son bouclier expiré : éclair 109 + laser 162… trop tard.

## Analyse
- Écart de 8 niveaux : le matchmaking (talent 528+) nous oppose à des poireaux bien plus avancés.
- Contre Solidification + boucliers (~130 par coup), nos attaques sont nulles pendant 3 tours.

## Correction
- `shouldWaitOutShield` : si le bouclier absolu adverse ≥ 40, expire dans ≤ 2 tours, que nos dégâts
  prévus < 40 % du potentiel sans bouclier et qu'une case hors de sa portée existe → on se met à l'abri
  au lieu d'attaquer (durée lue via `getEffects`).
