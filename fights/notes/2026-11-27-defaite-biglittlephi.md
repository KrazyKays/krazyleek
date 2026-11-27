# Défaite contre BigLittlePhi (joueur, niv. 43) — 54977259

- Lui : 630 PV, force 190, résistance 32, 10 PT, 4 PM (+2 bottes), fusil à pompe + magnum,
  éclair, flamme, bouclier, **Solidification**, protéines, motivation, bottes, bandage.
- Nous (niv. 40) : 677 PV, 11 PT, **4 PM** (4ᵉ PM acheté). Défaite au tour 6 : 396 infligés / 677 subis.

## Ce qui s'est passé
- T2 : Solidification (+184 résistance, 3 tours), T3 : Bouclier → **bouclier absolu 63 par coup** (T3–T5).
  Nos dégâts s'effondrent : flamme ≈ 33, éclair ≈ 41–71, mitraillette/caillou/étincelle ≈ 0.
- Fusil à pompe : **vulnérabilité absolue 25** sur nous à chaque tir → notre casque (15) annulé,
  bouclier (20) annulé. 7 PT de boucliers perdus au T3.

## Corrections
- `gen_items.py` : nouvelle colonne `I_ABSVULN` (vulnérabilité absolue infligée).
- Boucliers évalués à `bouclier × (1 + résistance/100) − vulnérabilité adverse` par coup
  (`effectiveShieldPerHit`) ; non lancés s'ils sont annulés.

## Pistes (non codées)
- **Attendre la fin du bouclier adverse** : quand nos dégâts prévus sont très inférieurs au potentiel
  sans bouclier, se mettre hors de portée 1–2 tours (nécessite de lire la durée restante via `getEffects`).
- **Libération** (niv. 60, 90 000 habs) : retire Solidification et le bouclier d'un coup.
- Contre gros bouclier : privilégier les gros coups uniques (rocher, éclair) — déjà fait par le calcul.
