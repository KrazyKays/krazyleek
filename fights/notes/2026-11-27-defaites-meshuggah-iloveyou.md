# 54978826 (Meshuggah777, niv. 50, poison) et 54978831 (ILOVEYOU, niv. 46)

> Correction : l'utilisateur confirme que ces combats incluaient les dernières mises à jour (sauf le
> nouveau `main`, ajouté après).

## 54978826 — MIXTE
- Même build poison que SoulFly777 (force 0, magie 300) : 776 PV perdus en poison.
- Boucliers au T2/T3 : **justifiés** (aucune attaque possible ; ils ont absorbé ses tirs de double pistolet
  ~21/coup, cf. « double_gun [0] »).
- Vrai problème : il garde ses distances (5 PM + bottes) et l'approche prudente évitait de finir à découvert.
  Contre le poison, c'est l'inverse qu'il faut : foncer. Correction : `isPoisoner` (magie > force) →
  approche sans pénalité d'exposition.

## 54978831 — ÉVITABLE (défaite à ~20 PV, adversaire +3 niveaux, build quasi identique au nôtre)
- T2 : plan défensif (Solidification + bouclier + casque) → bon (ses 4 étincelles du T3 absorbées),
  MAIS le poireau est resté sur place (repli après un plan sans dégâts).
- T3 : aucune case de tir atteignable → 13 PT perdus. Un tour d'attaque (~250) suffisait pour gagner.
- Correction : après un plan purement défensif, `approachAttackPosition` (approche prudente) au lieu
  du repli.
