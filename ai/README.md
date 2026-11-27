# IA

- `main.leek` : point d'entrée de krazyKlick, orchestre les modules.
- `lib/items.leek` : **généré** par `tools/gen_items.py` (données officielles des armes et puces).
- `lib/utils.leek` : debug et mesures.
- `lib/chips.leek` : utilisation sûre des puces (`tryChip`, `tryChipSelf`, `spamChip`).
- `lib/threat.leek` : coffres (ne jamais les réveiller, éviter les coffres réveillés, les achever si possible).
- `lib/team.leek` : combats d'équipe (tirs amis, cible commune par messages, soins des alliés, menaces multiples). **Inactif en solo.**
- `lib/summons.leek` : invocation des bulbes (case devant nous, 2 max) et IA générique du bulbe (soigne / protège / booste le poireau, puis attaque). **Inactif sans puce d'invocation.**
- `lib/targeting.leek` : choix de la cible (jamais un coffre, invocations en dernier).
- `lib/planner.leek` : choix de la case et de la combinaison d'attaques (sac à dos sur les PT).
- `lib/survival.leek` : soins et puces de soutien avec les PT restants.
- `lib/movement.leek` : approche à couvert et repli hors de vue.

L'IA lit l'équipement réellement porté : acheter/équiper une arme ou une puce ne demande
aucune modification du code (seules les puces de buff/soutien sont listées explicitement
dans `planner.leek` et `survival.leek`).
- `legacy/` : anciennes IA (Python), pour référence.

Sur Leek Wars, recréer la même arborescence dans l'éditeur (dossier `lib`, fichiers nommés
`utils.leek`, `chips.leek`…). Les `include` doivent contenir le chemin **avec l'extension** :
`include("lib/utils.leek")` (confirmé en jeu le 2026-11-26).

Les coûts, portées et recharges des puces ne sont jamais codés en dur : ils sont lus en combat
(`canUseChip`, `getChipCost`…).
