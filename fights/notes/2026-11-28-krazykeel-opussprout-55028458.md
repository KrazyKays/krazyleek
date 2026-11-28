# 55028458 — KrazyKeel (niv. 3) contre OpusSprout (niv. 3) : défaite, adversaire à 61 PV

**Verdict : ÉVITABLE (en partie).**
- Les deux bots attendent hors de portée (T4–T5). Notre limite de 2 tours atteinte, KrazyKeel entre à 5 cases
  au T6 sans ligne de vue → OpusSprout s'avance et tire le premier (66). Ensuite échange de pistolets.
- OpusSprout a 30 de force : ≈ 23 par tir contre ≈ 17 pour nous. Avec la première salve, il gagne de peu.
- KrazyKeel n'a **aucune puce** (shock niv. 2, bandage niv. 3 non achetés) : un bandage (+26 PV) suffisait à gagner.

## Correction (`ai/lib/movement.leek`)
Fin d'attente → `advanceUnderCover` : avancer vers lui en s'arrêtant sur une case **hors de sa ligne de vue**
(distance strictement décroissante, donc pas de boucle) ; à défaut, approche normale.
