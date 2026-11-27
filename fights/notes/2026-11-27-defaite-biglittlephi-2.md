# 2ᵉ défaite contre BigLittlePhi (niv. 43) — 54977580 (IA sans les 2 derniers correctifs)

- Mort au tour 8 : 294 infligés / 794 subis. Adversaire niveau 43 (nous 42).

## Ce qu'il fait (joueur malin)
- T2 Solidification (+199 rés.). T3 il **ne fait rien** (12 PT gardés) pendant qu'on lance
  Solidification + bouclier (57) + casque (43) à ~10 cases.
- T4 bottes + protéines + 6 cases + bouclier (66) ; il frappe aux T5–T8 (fusil à pompe : −25 sur nos boucliers).
  → Il « appâte » nos boucliers et attend qu'ils s'usent.

## Nos tours vides
- T4 (13 PT, ~7 cases), T6 (9 PT, ~4 cases : probablement l'attente du bouclier adverse 66),
  T8 (7 PT, ~3 cases, **aucun déplacement**, son bouclier était expiré) : cause inconnue → logs `[plan]` demandés.

## Correction
- Attente du bouclier : si après le repli il peut encore nous atteindre, on attaque quand même.

## Cause des tours vides (confirmée par les logs : « aucune attaque possible » aux T4, T6, T8)
Le meilleur plan était défensif (Solidification + Bouclier, 10 PT, 0 dégât) ; `chooseAttackCell` jetait les
plans sans dégâts → aucun plan → pas de déplacement (déjà sur une case d'attaque) → en fin de tour, après le
bandage, 9 PT < 10 pour Solidification + Bouclier, et bouclier/casque seuls annulés par le fusil à pompe (−25).
Corrigé : un plan est gardé s'il a des dégâts ou des puces sur soi.
