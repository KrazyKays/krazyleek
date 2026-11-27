# Outils

| Outil | Rôle |
|---|---|
| `fetch_api_data.py` | Télécharge puces, armes, constantes et fonctions dans `docs/data/` |
| `gen_items.py` | Génère `ai/lib/items.leek` (données des armes/puces pour l'IA) |
| `unlocks.py <de> <à> --force N` | Armes, puces et composants débloqués entre deux niveaux (dégâts/PT, prix) |
| `analyze_fight.py <id>` | Déroulé d'un combat + DIAGNOSTIC (évitable / écart de niveau / mixte) |
| `check_api.py` | Vérifie que le code `ai/` n'utilise que des fonctions/constantes existantes et non dépréciées |

## À venir

| Outil | Statut | Prérequis |
|---|---|---|
| `sync` : push/pull des IA via l'API Leek Wars, vérif de compilation | à faire | token API (formulaire sécurisé, jamais en clair) + accès réseau à leekwars.com |
| `simulate` : combats locaux en masse via leek-wars-generator (Java) | à faire | Java, clone du générateur |
| `optimize` : boucle variante → simulation → comparaison | à faire | `simulate` |
