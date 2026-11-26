# IA

- `main.leek` : point d'entrée, orchestre les modules.
- `lib/utils.leek` : debug et mesures.
- `lib/targeting.leek` : choix de la cible.
- `lib/combat.leek` : armes et puces.
- `lib/movement.leek` : approche et repli.

Sur Leek Wars, recréer la même arborescence dans l'éditeur (dossier `lib`) pour que les
`include("lib/...")` fonctionnent. L'extension `.leek` est locale : sur le site, l'IA s'appelle
juste `utils`, `targeting`, etc.

IA de démarrage générique : à adapter au build décrit dans `docs/context/profile.md`.
