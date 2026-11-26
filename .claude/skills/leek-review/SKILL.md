---
name: leek-review
description: Relire une IA LeekScript (Leek Wars) pour trouver bugs, gaspillage de PT/PM, dépassement d'opérations et cas limites. À utiliser quand on demande de relire, auditer, vérifier ou améliorer une IA dans ai/.
---

# Relecture d'une IA LeekScript

Cible : le fichier passé en argument, sinon `ai/main.leek` et tous les modules qu'il inclut.

## Checklist
1. **API** : chaque fonction appelée existe-t-elle dans `docs/leekscript/api-reference.md` ?
   Signaler toute fonction inconnue ou marquée *(à vérifier)*.
2. **Opérations** : boucles imbriquées, `getPathLength` ou `lineOfSight` répétés sur beaucoup de
   cases, recalculs évitables → estimer le coût et proposer un cache.
3. **Ressources** : PT non dépensés en fin de tour, `setWeapon` inutile, PM gaspillés,
   ordre déplacement/attaque sous-optimal.
4. **Robustesse** : cible morte en cours de tour, `null` (pas d'ennemi, pas d'arme),
   boucles sans garde, codes retour ignorés, `global` mal initialisée.
5. **Stratégie** : cohérence avec `docs/context/profile.md` (portée des armes vs déplacement,
   puces jamais utilisées, cooldowns ignorés).
6. **Pièges connus** : comparer à `docs/leekscript/pitfalls.md`.

## Format du rapport
Liste triée par gravité : **bloquant** (crash/IA qui ne joue pas) → **important** (perte de
dégâts/survie) → **mineur** (style, lisibilité). Pour chaque point : fichier:ligne, problème,
scénario concret, correctif proposé. Ne modifier le code que si l'utilisateur le demande.
Si un nouveau piège général est trouvé, proposer de l'ajouter à `pitfalls.md`.
