# IA actuelle de krazyKlick (version d'origine, conservée telle quelle pour référence)
# PISTOLET
# Motivation, Bandage, Casque, Proteine, Caillou, Etincelle
me = Fight.me
enemy = None

enemies = Fight.getAliveEnemies()
real_enemies = [e for e in enemies if not isinstance(e, Chest)]
targets = real_enemies if real_enemies else enemies

if targets:
    enemy = targets[0]

if enemy is not None:

# GOGOGOOOOOOOOOOOOOOOOOOOOOOOOOOOO

    me.moveToward(enemy)

# MO TI VA TION, YOU CAN DO IT !

    if Chip.motivation.currentCooldown == 0:
        if me.tp >= Chip.motivation.cost:
            me.useChip(Chip.motivation)

# PRESENTEZ ....... ARME !

    if me.weapon is not Weapon.pistol:
        me.setWeapon(Weapon.pistol)

    distance = me.distance(enemy)
    los = me.cell.lineOfSight(enemy.cell)
    weapon_cost = me.weapon.cost

# BOBO ????????????????????????

    if me.life < (me.maxLife - 28):
        if Chip.bandage.currentCooldown == 0:
            if me.tp >= Chip.bandage.cost:
                me.useChip(Chip.bandage)

# PREPARE FOR BATTLEEEEEEEEEEEE

    if distance <= 10:
        if Chip.helmet.currentCooldown == 0:
            if not los or distance > 7:
                if me.tp >= Chip.helmet.cost:
                    me.useChip(Chip.helmet)
            elif me.tp >= Chip.helmet.cost + weapon_cost:
                me.useChip(Chip.helmet)
        if Chip.protein.currentCooldown == 0:
            if not los or distance > 7:
                if me.tp >= Chip.protein.cost:
                    me.useChip(Chip.protein)
            elif me.tp >= Chip.protein.cost + weapon_cost:
                me.useChip(Chip.protein)

# FEUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

    if los and distance <= 7:
        if distance <= 5:
            if Chip.pebble.currentCooldown == 0:
                if me.tp >= Chip.pebble.cost + weapon_cost:
                    me.useChip(Chip.pebble, enemy)
        while me.canUseWeapon(enemy) and me.tp >= me.weapon.cost:
            me.useWeapon(enemy)
    elif distance <= 10:
        if Chip.spark.currentCooldown == 0:
            while me.tp >= Chip.spark.cost:
                me.useChip(Chip.spark, enemy)
