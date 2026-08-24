import copy
import random


def report_hazards(unit, hazards, dead,verbose = False):
    if hazards > 0 and dead == 0:
        print(f"  suffered {dead*unit.hp+hazards} damage from HAZARDOUS\n")
    elif dead > 0:
        print(f"  suffered {dead*unit.hp+hazards} damage from HAZARDOUS, {dead} models die\n")
    else:
        print("")

def damage(dmg, verbose = False):
    if type(dmg) is int:
        return dmg
    if "+" in dmg:
        a = dmg.split("+")
        return (random.randint(1,int(a[0][1:]))+int(a[1]))
    else:
        return (random.randint(1,int(dmg[1:])))

def deal_damage(unit, target, dmg, x,y,z, verbose = False):
    if unit.fortyk:
        x += dmg
        y -= dmg
        if y<1:
            y = target.hp
            z += 1
    if unit.aos:
        x += dmg
        dmg += y
        while dmg >= target.hp:
            dmg -= target.hp
            z += 1
        y = dmg
    return x,y,z

def do_it(unit, target, x=0, y=0, z=0, melee=None, strike=False, hazards = None, dead = None,verbose = False):
    if y == 0:
        y = target.hp
    crit = False
    for wep in unit.weapons:
        hits = 0
        wounds = 0

        if verbose:
            print(f"attacking with weapon profile:\n{wep}\n====================================")

        if "charge(+1 dmg)" in wep[6]:
            wep[5] += 1

        if strike is True and "strike" in wep[6]:
            strike = False
            continue

        shots = 0
        if type(wep[1]) is int:
            shots = wep[1]*wep[0]
        else:
            if len(wep[1].split("+"))>1:
                shoots = wep[1].split("+")[0]
                ex = int(wep[1].split("+")[1])
            else:
                shoots = wep[1]
                ex = 0
            if len(shoots.split("d")[0]) == 0:
                for i in range(0, wep[0]):
                    shots += random.randint(1, int(shoots.split("d")[1]))+ex
            else:
                for i in range(0, wep[0]*int(shoots.split("d")[0])):
                    shots += random.randint(1, int(shoots.split("d")[1]))+ex

        if "rapid_fire" in wep[6]:
            shots += wep[6]["rapid_fire"]*wep[0]

        if verbose:
            print(f"nonblast attacks: {shots}")

        if "blast" in wep[6]:
            for i in range (4, target.models *2, 5):
                shots += wep[6]["blast"]*wep[0]

        if verbose:
            print(f"Total attacks: {shots}")

        checks = 0

        to_hit = wep[2]
        if "heavy" in wep[6]:
            to_hit = wep[2]-1
            if to_hit <2:
                to_hit = 2


        if wep[2] == "torrent":
            if verbose:
                print("torrent hits automatically")
            hits = shots
        else:
            for i in range(0, shots):
                crit = False
                hit=random.randint(1,6)
                if verbose:
                    print(f"rolled {hit} to hit")
                if hit == 1 and "hazardous" in wep[6]:
                    checks += 1
                if hit == 6 or (hit > 3 and "conversion" in wep[6]):
                    crit = True
                    if verbose:
                        print("crit")

                if hit >= to_hit or crit:
                    if crit and ("lethal_hits" in wep[6] or "crit(auto-wound)" in wep[6]):
                        if verbose:
                            print("lethal")
                        wounds += 1
                    elif crit and "crit(mortal)" in wep[6]:
                        mortals = damage(wep[5], verbose = verbose)
                        if verbose:
                            print(f"crit mortal:{mortals}")
                        dmg = 0
                        if target.fnp < 7:
                            for i in range (mortals):
                                fnpm1 = random.randint(1,6)
                                if verbose:
                                    print(f"feelnopain: {fnpm1}")
                                if fnpm1 < unit.fnp:
                                    dmg += 1
                        else:
                            dmg = mortals
                        x,y,z = deal_damage(unit, target, dmg, x,y,z, verbose = verbose)
                    else:
                        if verbose and not crit:
                            print("hit")
                        hits += 1

                    if crit and "crit(2 hits)" in wep[6]:
                        if verbose:
                            print("crit 2 hits")
                        hits += 1
                    if crit and "sustained_hits" in wep[6]:
                        if verbose:
                            print("sustained")
                        extra = wep[6]["sustained_hits"]
                        if type(extra) is not int:
                            extra = random.randint(1,int(extra[1]))
                            if verbose:
                                print(f"extra {extra} hits")
                        hits += extra

        if verbose:
            print(f"total hits: {hits}\n====================================")

        if unit.fortyk:
            if wep[3] == target.toughness:
                to_wound = 4
            if wep[3] > target.toughness:
                to_wound = 3
            if wep[3] < target.toughness:
                to_wound = 5
            if wep[3] >= 2*target.toughness:
                to_wound = 2
            if 2*wep[3] <= target.toughness:
                to_wound = 6
            if "anti_vehicle" in wep[6] and "vehicle" in target.kw:
                to_wound = wep[6]["anti_vehicle"]
            if "anti_infantry" in wep[6] and "infantry" in target.kw:
                to_wound = wep[6]["anti_infantry"]
            if "anti_character" in wep[6] and "character" in target.kw:
                to_wound = wep[6]["anti_character"]
            if "anti_psyker" in wep[6] and "psyker" in target.kw:
                to_wound = wep[6]["anti_psyker"]
        if unit.aos:
            to_wound = wep[3]
            if "anti-infantry" in wep[6] and "infantry" in target.kw:
                wep[4] += 1
            if "anti-hero" in wep[6] and "hero" in target.kw:
                wep[4] += 1
            if "anti-monster" in wep[6] and "monster" in target.kw:
                wep[4] += 1
            if "anti-cavalry" in wep[6] and "cavalry" in target.kw:
                wep[4] += 1
            if "anti-wizard" in wep[6] and "wizard" in target.kw:
                wep[4] += 1
            if "anti-priest" in wep[6] and "priest" in target.kw:
                wep[4] += 1
            if "anti-beast" in wep[6] and "beast" in target.kw:
                wep[4] += 1
            if "anti-war_machine" in wep[6] and "war_machine" in target.kw:
                wep[4] += 1
            if "anti-manifestation" in wep[6] and "manifestation" in target.kw:
                wep[4] += 1

        if "lance" in wep[6]:
            print("Lance active (+1 to wound)")
            to_wound -= 1
            if to_wound < 2:
                to_wound = 2

        if verbose and unit.fortyk:
            print(f"to wound needed: {to_wound}")

        for i in range(0, hits):
            wound = random.randint(1,6)
            if verbose:
                print(f"rolled {wound} to wound")
            if wound<to_wound and "twin-linked" in wep[6]:
                wound = random.randint(1,6)
                if verbose:
                    print(f"reroll for twin-linked: {wound}")
            if wound >= to_wound:
                if wound == 6 and "devastating_wounds" in wep[6]:
                    mortals = damage(wep[5], verbose = verbose)
                    if "melta" in wep[6]:
                        mortals += wep[6]["melta"]
                    if verbose:
                        print(f"devastating wound: {mortals} damage")
                    dmg = 0
                    if target.fnpm < 7:
                        for i in range (mortals):
                            fnpm1 = random.randint(1,6)
                            if verbose:
                                print(f"feel no pain: {fnpm1}")
                            if fnpm1 < target.fnpm:
                                dmg += 1
                    else:
                        dmg = mortals
                    x,y,z = deal_damage(unit, target, dmg, x,y,z,verbose = verbose)
                else:
                    wounds += 1

        to_save = target.save+wep[4]
        if melee is None and target.cover == 1 and "ignore cover" not in wep[6]:
            if wep[4] > 0:
                to_save -= 1
                if verbose:
                    print("cover bonus")
            else:
                if target.save > 3:
                    to_save -= 1
                    if verbose:
                        print("cover bonus")
        to_save -= unit.stealth
        if to_save < 2:
            to_save = 2

        if verbose:
            print(f"total wounds: {wounds}\n====================================")
            print(f"to_save needed: {to_save}")

        for i in range(0, wounds):
            save = random.randint(1,6)
            if verbose:
                print(f"save rolled: {save}")

            if save < to_save and save < target.invul:
                dmag = damage(wep[5], verbose = verbose)
                if "melta" in wep[6]:
                    dmag += wep[6]["melta"]
                if verbose:
                    print(f"damage dealt: {dmag}")
                dmg = 0
                if target.fnp < 7:
                    for i in range (dmag):
                        fnp1 = random.randint(1,6)
                        if verbose:
                            print(f"feel no pain: {fnp1}")
                        if fnp1 < target.fnp:
                            dmg += 1
                else:
                    dmg = dmag
                x,y,z = deal_damage(unit, target, dmg, x,y,z,verbose = verbose)

        if unit.aos:
            if "anti-infantry" in wep[6] and "infantry" in target.kw:
                wep[4] -= 1
            if "anti-hero" in wep[6] and "hero" in target.kw:
                wep[4] -= 1
            if "anti-monster" in wep[6] and "monster" in target.kw:
                wep[4] -= 1
            if "anti-cavalry" in wep[6] and "cavalry" in target.kw:
                wep[4] -= 1
            if "anti-wizard" in wep[6] and "wizard" in target.kw:
                wep[4] -= 1
            if "anti-priest" in wep[6] and "priest" in target.kw:
                wep[4] -= 1
            if "anti-beast" in wep[6] and "beast" in target.kw:
                wep[4] -= 1
            if "anti-war_machine" in wep[6] and "war_machine" in target.kw:
                wep[4] -= 1
            if "anti-manifestation" in wep[6] and "manifestation" in target.kw:
                wep[4] -= 1

        if verbose and "hazardous" in wep[6]:
            print(f"hazard checks total: {checks}")
            print(f"{hazards} dmg in model")
            print(f"{dead} dead so far")
        if hazards is None:
            hazards = 0
        if dead is None:
            dead = 0
        for i in range (0, checks):
            check = random.randint(1,6)
            if verbose:
                print(f"hazard roll: {check}")
            if check == 1:
                hazards += 1
                if "character" in unit.kw or "vehicle" in unit.kw or "monster" in unit.kw:
                    hazards += 2
        temp = unit.hp
        while (hazards > 0):
            hazards -= 1
            check = random.randint(1,6)
            if check < unit.fnpm:
                temp -= 1
                if temp < 1:
                    temp = unit.hp
                    dead += 1

        if "charge(+1 dmg)" in wep[6]:
            wep[5] -= 1

        if "strike" in wep[6]:
            strike =True

        if verbose:
            print("")

    if len(unit.ranged_weapons5) == 0:
        temp = unit.hp
        dead = 0

    return x,y,z,strike,unit.hp-temp,dead

def repeat_with_sweep(unit,target, x=0, y=0, z=0, xx= 0, yy = 0, zz = 0,allin = False, hazards = None, dead = None, verbose = False):
    if y == 0:
        y = target.hp
    if yy == 0:
        yy = target.hp

    for item in unit.weapons:
        if "strike" in item[6]:
            item[0] = 0
        if "sweep" in item[6]:
            item[0] = 1
    xx,yy,zz,strike,hazards, dead = do_it(unit, target,xx,yy,zz,melee=True,strike=True, hazards = hazards, dead = dead, verbose = verbose)
    if allin is False:
        print(f"{unit.models} man {unit.name} deals {xx} damage to {target.name} using Sweep \n killing {zz} models.")
        report_hazards(unit, hazards, dead, verbose = verbose)

    for item in unit.weapons:
        if "strike" in item[6]:
            item[0] = 1
        if "sweep" in item[6]:
            item[0] = 0
    return False, xx,yy,zz,hazards, dead

def shoot(unit, target, x=0, y=0, z=0, verbose = False):
    if y == 0:
        y=target.hp

    print("Shooting:")

    unit.weapons = unit.ranged_weapons5

    x,y,z,ignore,hazards, dead = do_it(unit,target,x,y,z, verbose = verbose)

    if unit.models != 1:
        print(f"{unit.models} man {unit.name} deals {x} damage to {target.name}\n killing {z} models")
    else:
        print(f"{unit.name} deals {x} damage to {target.name}\n killing {z} models")
    report_hazards(unit, hazards, dead, verbose = verbose)

    if unit.models != 1:

        unit.weapons = unit.ranged_weapons10
        x,y,z,ignore,hazards,dead = do_it(unit,target,x,y,z,hazards = hazards, dead = dead, verbose = verbose)

        print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name}\n killing {z} models")
        report_hazards(unit, hazards, dead, verbose = verbose)

    return x,y,z, hazards, dead

def melee(unit, target, x=0, y=0, z=0, xx=0, yy = 0, zz = 0, allin = False,hazards = None, dead = None, verbose = False):
    if allin is False:
        x=0
        y=target.hp
        z=0
    if y == 0:
        y = target.hp
    if yy == 0:
        yy = target.hp
    striked = False

    print("Melee combat:")

    unit.weapons = unit.melee_weapons5

    x,y,z,strike,hazards,dead = do_it(unit,target,x,y,z, melee=True,hazards = hazards, dead = dead, verbose = verbose)

    if strike is False:
        if unit.models != 1:
            if allin is False:
                print(f"{unit.models} man {unit.name} deals {x} damage to {target.name}\n killing {z} models.")
                report_hazards(unit, hazards, dead, verbose = verbose)
        else:
            if allin is False:
                print(f"{unit.name} deals {x} damage to {target.name}\n killing {z} models.")
                report_hazards(unit, hazards, dead, verbose = verbose)
    else:
        if unit.models != 1:
            if allin is False:
                print(f"{unit.models} man {unit.name} deals {x} damage to {target.name} using Strike \n killing {z} models.")
                report_hazards(unit, hazards, dead, verbose = verbose)
            strike, xx, yy, zz,hazards,dead = repeat_with_sweep(unit, target, x,y,z,xx, yy, zz, allin = allin,hazards = hazards, dead = dead, verbose = verbose)
        else:
            if allin is False:
                print(f"{unit.name} deals {x} damage to {target.name} using Strike \n killing {z} models.")
                report_hazards(unit, hazards, dead, verbose = verbose)
            strike, xx, yy, zz,hazards, dead = repeat_with_sweep(unit, target, x,y,z,xx, yy, zz, allin = allin, hazards = hazards, dead = dead, verbose = verbose)
            striked = True

    if unit.models != 1:

        unit.weapons = unit.melee_weapons10
        x,y,z,strike,hazards, dead = do_it(unit,target,x,y,z,melee=True, hazards = hazards, dead = dead,verbose = verbose)

        if strike is False:
            if allin is False:
                print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name}\n killing {z} models")
                report_hazards(unit, hazards, dead, verbose = verbose)
        else:
            if allin is False:
                print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name} using Strike\n killing {z} models")
                report_hazards(unit, hazards, dead, verbose = verbose)
            strike, xx, yy, zz,hazards, dead = repeat_with_sweep(unit, target, allin=allin, hazards = hazards, dead = dead,verbose = verbose)
        print("")

    return x,y,z,xx,yy,zz,striked,hazards, dead

def all_in(unit, target, verbose=False):
    print(f"{unit.name} goes all-in on {target.name}:")
    x = 0
    y = 0
    z = 0
    x, y, z,hazards, dead = shoot(unit, target, verbose = verbose)
    xx = copy.copy(x)
    yy = copy.copy(y)
    zz = copy.copy(z)

    x, y, z, xx, yy, zz, striked,hazards, dead = melee(unit, target, x, y, z, xx, yy, zz, allin = True,hazards = hazards, dead = dead, verbose = verbose)

    if striked:
        print(f"{unit.name} does {x} damage in total using Strike\n killing {z} models")
        report_hazards(unit, hazards, dead, verbose = verbose)
        print(f"{unit.name} does {xx} damage in total using Sweep\n killing {zz} models")
        report_hazards(unit, hazards, dead, verbose = verbose)
    else:
        print(f"{unit.name} does {x} damage to {target.name}\n killing {z} models")
        report_hazards(unit, hazards, dead, verbose = verbose)
