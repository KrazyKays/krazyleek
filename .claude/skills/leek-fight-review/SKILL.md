---
name: leek-fight-review
description: Analyser un combat Leek Wars (lien leekwars.com/fight/… ou /report/…) et classer le résultat : défaite évitable (erreur de l'IA à corriger) ou due à l'écart de niveau / d'équipement. À utiliser dès que l'utilisateur envoie un lien de combat.
---

# Analyse d'un combat

1. `python3 tools/analyze_fight.py <id>` : déroulé + section **DIAGNOSTIC** (verdict automatique).
2. Relire le déroulé pour confirmer ou corriger le verdict (le diagnostic est heuristique) :
   - **ÉVITABLE** : tours vides au contact, mauvaise cible, boucliers jamais / mal lancés, va-et-vient,
     match nul. → Trouver la cause dans le code, corriger, ajouter le piège à `docs/leekscript/pitfalls.md`.
     Si la cause n'est pas visible dans les actions, demander les lignes `[plan]` / `[exec]` du log.
   - **ÉCART DE NIVEAU** (adversaire ≥ 5 niveaux au-dessus, sans erreur IA) : ne PAS sur-adapter le code
     à ce combat. Expliquer ce qui manque (stats, objets adverses) et quand on l'aura (`tools/unlocks.py`).
   - **MIXTE** : corriger uniquement la part IA, et le dire clairement.
   - **NIVEAU PROCHE SANS ERREUR** : piste build / équipement → proposer un ajustement de setup.
3. Toujours annoncer le verdict en tête de la réponse (Évitable / Écart de niveau / Mixte).
4. Écrire `fights/notes/AAAA-MM-JJ-<sujet>.md` avec le verdict, le déroulé clé, les causes, les corrections.
5. Si le combat montre que notre niveau a changé par rapport à `docs/context/profile.md` :
   appliquer aussi le skill `leek-levelup`.
