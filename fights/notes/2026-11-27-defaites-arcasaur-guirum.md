# Arcasaur (54983922) et Guirum (54983936) — niv. 50

## 54983922 — Arcasaur : ÉCART DE NIVEAU (poison + kite)
- Force 20, magie 170, 14 PT, 5 PM : **869 de nos 908 PV perdus en poison** ; il soigne et recule.
- Nous : 268 infligés ; T8–T9 sans attaque (il est hors de portée après son repli). Coffre en bois ignoré (bien).
- Réponse : mobilité (Propulseur / 5ᵉ PM) et étincelle, cf. « Niveau 45 ».

## 54983936 — Guirum : MIXTE, avec un vrai bug IA
- Guirum reste immobile (case 67), se soigne (soin + bandage ~100 PV/tour) et invoque **8 bulbes**.
- Nous : immobiles à 5 cases (case 82) pendant ~45 tours, sans attaquer : les bulbes bloquent passage et
  ligne de vue ; l'IA ignore les invocations tant qu'un poireau adverse vit. Les bulbes nous infligent ~580.
- Correction : `fallbackAttack` (lib/targeting.leek) : si la cible principale est inattaquable ce tour,
  frapper le meilleur autre ennemi atteignable (bulbe compris, kill en priorité ; 3 plus proches max
  pour le budget d'opérations). Jamais un coffre.
