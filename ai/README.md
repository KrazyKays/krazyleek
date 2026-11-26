# IA

- `main.leek` : point d'entrée de krazyKlick, orchestre les modules.
- `lib/utils.leek` : debug et mesures.
- `lib/chips.leek` : utilisation sûre des puces (`tryChip`, `tryChipSelf`, `spamChip`).
- `lib/targeting.leek` : choix de la cible (coffres en dernier).
- `lib/combat.leek` : séquence caillou → pistolet → étincelle.
- `lib/survival.leek` : bandage et casque.
- `lib/movement.leek` : approche et repli.
- `legacy/` : anciennes IA (Python), pour référence.

Sur Leek Wars, recréer la même arborescence dans l'éditeur (dossier `lib`, fichiers nommés
`utils.leek`, `chips.leek`…). Les `include` doivent contenir le chemin **avec l'extension** :
`include("lib/utils.leek")` (confirmé en jeu le 2026-11-26).

Les coûts, portées et recharges des puces ne sont jamais codés en dur : ils sont lus en combat
(`canUseChip`, `getChipCost`…).
