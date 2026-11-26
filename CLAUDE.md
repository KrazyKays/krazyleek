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
| `docs/game/` | Mécaniques de jeu (formules, caractéristiques, tour de jeu). |
| `docs/context/` | Profil du joueur : poireaux, builds, équipement, stratégie. **À lire avant d'écrire une IA.** |
| `tools/` | Scripts (sync API, simulateur local, analyse de combats). |
| `fights/` | Données de combats téléchargées (ignorées par git sauf `fights/notes/`). |
| `.claude/skills/` | Skills : `/leek-write`, `/leek-review`. |
| `.claude/agents/` | Agents spécialisés (`leek-strategist`). |

## Règles pour écrire du LeekScript
1. **Ne jamais inventer une fonction de l'API.** Vérifier dans `docs/leekscript/api-reference.md`.
   Si une fonction n'y est pas, le signaler et marquer `// TODO vérifier` plutôt que deviner.
   Les entrées marquées *(à vérifier)* dans la doc ne sont pas encore confirmées.
2. **Budget d'opérations** : chaque tour a une limite d'opérations. Éviter les boucles
   imbriquées sur toutes les cellules (613 cases) sans cache. Mesurer avec `getOperations()`.
3. **Toujours tester le code retour** de `useWeapon` / `useChip` (`USE_SUCCESS`, etc.)
   avant d'enchaîner d'autres actions.
4. Une responsabilité par module dans `ai/lib/` ; `main.leek` ne fait qu'orchestrer.
5. Les variables qui doivent survivre entre les tours sont déclarées `global`.
6. Mettre à jour `docs/leekscript/pitfalls.md` dès qu'on découvre un piège ou un bug.

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
- [ ] `tools/` : sync avec l'API Leek Wars (nécessite un token, via le formulaire sécurisé — jamais en clair).
- [ ] `tools/` : simulateur local (leek-wars-generator) pour des combats en masse.
- [ ] Analyse automatique des combats + boucle d'optimisation.
