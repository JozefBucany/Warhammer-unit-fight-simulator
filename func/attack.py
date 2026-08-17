import random


def shoot(unit, target):
    x = 0

    for i in range(0, unit.shots*5):
        hit=random.randint(1,6)
        if hit >= unit.BS:
            x+=unit.ranged_dmg

    print(f"5 man unit of {unit.name} deals {x} damage to unit {target.name}")

# 5-unit.amount-unit.apothecary
# unit.amount
# 10-unit.amount_10-unit.apothecary
# unit.amount_10
# unit.ranged_str
# unit.ranged_ap
# unit.ranged_dmg
# unit.ranged_ability

# target.toughness
# target.save



    return


def melee(unit, target):
    x = 0

    for i in range(0, unit.attacks*5):
        hit=random.randint(1,6)
        if hit >= unit.WS:
            x+=unit.melee_dmg

    print(f"5 man unit of {unit.name} deals {x} damage to unit {target.name}")

# unit.melee_str
# unit.melee_ap
# unit.melee_dmg
# unit.melee_ability

# target.toughness
# target.save



    return
