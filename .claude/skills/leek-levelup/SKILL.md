---
name: leek-levelup
description: Proposer de façon proactive un nouveau setup (puces, armes, composants, capital) quand krazyKlick monte de niveau. À utiliser dès que l'utilisateur annonce un niveau, une dépense de capital, un achat, ou qu'un combat montre un niveau supérieur à celui du profil.
---

# Montée de niveau → nouveau setup

1. Mettre à jour `docs/context/profile.md` (niveau, stats, équipement, capital) à partir de ce que dit
   l'utilisateur ou des données du dernier combat (`fights/<id>.json`, entrée `leeks`).
2. `python3 tools/unlocks.py <ancien_niveau> <nouveau_niveau + 10> --force <force>` :
   - ce qui vient d'être débloqué → à évaluer tout de suite ;
   - ce qui arrive dans les 10 prochains niveaux → à anticiper (économiser des habs / ressources).
3. Proposer un setup concret, sans attendre qu'on le demande :
   - armes (2 emplacements) et puces (emplacements = RAM) : quoi acheter, quoi retirer, pourquoi
     (dégâts/PT, portée, ligne de vue, synergies : Solidification × boucliers, protéines × dégâts) ;
   - composants à crafter (8 emplacements, `docs/data/components.json`) ;
   - capital : gain par point (voir `docs/game/build-recommendation.md` et `mechanics.md`).
   Tenir compte des adversaires récents (`fights/notes/`) : ce qui nous a battus à niveau proche.
4. Vérifier que l'IA sait utiliser les nouveaux objets (dégâts, soins, boucliers : automatique ;
   invocations, poison, entraves, Libération, téléportation : code à écrire → le proposer).
5. Consigner la recommandation dans `docs/game/build-recommendation.md` (section « Niveau N »).
