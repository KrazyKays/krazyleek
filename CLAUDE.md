# KrazyLeek — workspace IA Leek Wars

Ce repo sert d'atelier pour écrire, tester et optimiser des IA pour [Leek Wars](https://leekwars.com),
écrites en **LeekScript** (version cible : **v4**).

## Langue
- Échanges, docs et commentaires de code : **français**.
- Identifiants (variables, fonctions, classes) : anglais, camelCase.

## Arborescence
| Dossier | Rôle |
|---|---|
| `ai/` | Code des IA. `ai/main.leek` = point d'entrée, `ai/lib/` = modules inclus. |
| `docs/leekscript/` | Référence du langage et de l'API du jeu + pièges connus. |
| `docs/game/` | Mécaniques (formules), `equipment.md`, `build-recommendation.md`, `progression.md` (ce qui change en montant). |
| `docs/data/` | Données brutes de l'API Leek Wars (puces, armes, constantes, fonctions). |
| `docs/context/` | Profil du joueur : poireaux, builds, équipement, stratégie. **À lire avant d'écrire une IA.** |
| `tools/` | Scripts (sync API, simulateur local, analyse de combats, `xp_stats.py` : XP par mode). |
| `fights/` | Données de combats téléchargées (ignorées par git sauf `fights/notes/`). |
| `.claude/skills/` | Skills : `/leek-write`, `/leek-review`, `/leek-fight-review`, `/leek-levelup`. |
| `.claude/agents/` | Agents spécialisés (`leek-strategist`). |

## Règles pour écrire du LeekScript
1. **Ne jamais inventer une fonction de l'API.** Vérifier dans `docs/leekscript/api-reference.md`
   ou `docs/data/functions.json`, et lancer `python3 tools/check_api.py` après chaque modification.
   Si une fonction n'y est pas, le signaler et marquer `// TODO vérifier` plutôt que deviner.
   Les entrées marquées *(à vérifier)* dans la doc ne sont pas encore confirmées.
2. **Budget d'opérations** : chaque tour a une limite d'opérations. Éviter les boucles
   imbriquées sur toutes les cellules (613 cases) sans cache. Mesurer avec `getOperations()`.
3. **Toujours tester le code retour** de `useWeapon` / `useChip` (`USE_SUCCESS`, etc.)
   avant d'enchaîner d'autres actions.
4. Une responsabilité par module dans `ai/lib/` ; `main.leek` ne fait qu'orchestrer.
5. Les variables qui doivent survivre entre les tours sont déclarées `global`.
6. Mettre à jour `docs/leekscript/pitfalls.md` dès qu'on découvre un piège ou un bug.

## Réflexes permanents (demandés par l'utilisateur)
- **Chaque combat envoyé** → skill `leek-fight-review` : annoncer d'abord le verdict
  **Évitable** (erreur IA → corriger le code) / **Écart de niveau** (ne pas sur-adapter le code ;
  dire ce qui manque et quand on l'aura) / **Mixte**. Outil : `tools/analyze_fight.py` (section DIAGNOSTIC).
- **Chaque montée de niveau** (annoncée, ou visible dans un combat) → skill `leek-levelup` :
  proposer de soi-même un nouveau setup armes / puces / composants / capital (`tools/unlocks.py`).

## Workflow
1. Lire `docs/context/profile.md` (build et stratégie actuels).
2. Écrire/modifier le code (`/leek-write`).
3. Relire (`/leek-review`) : logique, coût en opérations, cas limites.
4. Tester en jeu (pour l'instant manuellement : copier le code dans l'éditeur Leek Wars).
5. Noter les enseignements des combats dans `fights/notes/`.

## État du projet
- [x] Squelette, docs de base, skills de relecture/écriture.
- [x] Profil joueur rempli (`docs/context/profile.md`).
- [x] Import de l'IA existante (`ai/legacy/`).
- [x] IA planificateur générique (`ai/lib/planner.leek`) + config recommandée (`docs/game/build-recommendation.md`).
- [x] `tools/gen_items.py` : génère `ai/lib/items.leek` (ne jamais l'éditer à la main).
- [x] `tools/fetch_api_data.py` (données publiques) et `tools/check_api.py` (validation du code).
- [ ] `tools/` : sync avec l'API Leek Wars (nécessite un token, via le formulaire sécurisé — jamais en clair).
- [ ] `tools/` : simulateur local (leek-wars-generator) pour des combats en masse.
- [x] Analyse de combats : `tools/analyze_fight.py <id>` (+ notes dans `fights/notes/`).
- [ ] Boucle d'optimisation automatique.
