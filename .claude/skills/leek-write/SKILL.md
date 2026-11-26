---
name: leek-write
description: Écrire ou modifier du code LeekScript (IA Leek Wars) dans ai/ en respectant les conventions du projet. À utiliser dès qu'on demande de créer une IA, un module, une stratégie ou une fonction pour Leek Wars.
---

# Écrire du LeekScript pour KrazyLeek

## Avant d'écrire
1. Lire `docs/context/profile.md` : build, armes, puces, stratégie. Si le profil est vide et que
   le besoin en dépend, demander les infos manquantes plutôt que supposer.
2. Lire `docs/game/equipment.md` (coûts, portées, dégâts réels), `docs/leekscript/api-reference.md` et `docs/leekscript/pitfalls.md`.
3. Lire les modules existants de `ai/lib/` pour réutiliser plutôt que dupliquer.

## Règles d'écriture
- LeekScript **v4**. Uniquement des fonctions présentes dans `api-reference.md`.
  Si une fonction nécessaire n'y est pas : la chercher dans la doc officielle
  (https://leekwars.com/help/documentation), l'ajouter à `api-reference.md` avec la mention
  *(à vérifier)* si non confirmée, et commenter `// TODO vérifier` dans le code.
- Une responsabilité par module dans `ai/lib/`. `main.leek` ne fait qu'orchestrer.
- Commentaires en français ; identifiants en anglais camelCase.
- Toute boucle `while` a une garde anti-boucle infinie.
- Tester les codes retour de `useWeapon` / `useChip`.
- Pas de parcours des 613 cases avec `getPathLength` sans cache : préférer `getCellDistance`
  pour pré-filtrer, puis le calcul exact sur les quelques candidats.
- État persistant entre tours → `global`.

## Après avoir écrit
- Lancer `python3 tools/check_api.py` et corriger toute fonction/constante inconnue ou dépréciée.
- Résumer : fichiers modifiés, logique, hypothèses non vérifiées.
- Proposer de lancer `/leek-review` sur le code modifié.
- Rappeler que le code se teste en le copiant dans l'éditeur Leek Wars (tant que `tools/` n'a pas de sync).
