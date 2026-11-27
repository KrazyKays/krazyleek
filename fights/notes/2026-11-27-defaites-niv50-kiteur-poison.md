# Deux défaites contre des niveaux 50 — 54978528 (Miroleek) et 54978532 (Whistleblower)

## 54978528 — Miroleek (niv. 50) : MIXTE
- Stats proches des nôtres (727 PV, force 210, 12 PT, 4 PM) : la différence vient surtout de son IA.
- Il fait du **tir et repli** : il avance, tire au laser (portée 9) ou à l'étincelle, puis recule.
  Nous : une seule attaque en 8 tours (T6 : 262) ; tours T4, T5, T8 sans attaque.
- Cause : sans attaque possible, on marchait droit vers la position d'attaque la plus proche et on
  finissait le tour à découvert, à sa portée ; il nous tirait dessus puis reculait.
- Correction : `approachAttackPosition` va directement sur une position d'attaque si elle est atteignable ce
  tour ; sinon, approche prudente (case la plus proche d'une position d'attaque en évitant de finir à
  découvert et à sa portée).

## 54978532 — Whistleblower (niv. 50) : ÉCART DE NIVEAU
- **Poison (Venin, empilé chaque tour) : 400 dégâts sur 766**, qui ignorent nos boucliers.
  Soins énormes (Connaissance + Soin : 211 PV en un tour), Stalactite, fusil à pompe.
- Nous : 911 dégâts infligés, aucune erreur ; il lui restait ~235 PV.
- Parades : Libération (niv. 60) retire une partie des effets ; Antidote seulement au niv. 114.
- `analyze_fight.py` compte maintenant les dégâts de poison (action 110).
