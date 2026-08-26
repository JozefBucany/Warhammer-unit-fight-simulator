import random


def report_hazards(unit, hazards, dead,verbose = False):
    if hazards > 0 and dead == 0:
        print(f"  suffered {dead*unit.hp+hazards} damage from HAZARDOUS\n")
    elif dead > 0:
        print(f"  suffered {dead*unit.hp+hazards} damage from HAZARDOUS, {dead} models die\n")
    else:
        print("")

def damage(dmg, verbose = False):
    result = 0
    if type(dmg) is int:
        result = dmg
    else:
        if len(dmg.split("+"))>1:
            dmg1 = dmg.split("+")[0]
            ex = int(dmg.split("+")[1])
        else:
            dmg1 = dmg
            ex = 0
        if len(dmg1.split("d")[0]) == 0:
            result += random.randint(1, int(dmg1.split("d")[1]))+ex
        else:
            for i in range(0, int(dmg1.split("d")[0])):
                result += random.randint(1, int(dmg1.split("d")[1]))+ex
    return result

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

def libi_buff(target, dmg,verbose = False):
    x = 0
    for i in range (dmg):
        roll = random.randint(1,6)
        if roll < target.fnpp:
            if verbose:
                print("i feel pain...")
            x += 1
        else:
            if verbose:
                print("i feel no pain!")
    return x

def do_it(unit, target, x=0, y=0, z=0, melee=False, strike=False, focused = False, hazards = None, dead = None,verbose = False):
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
        if focused is True and "focused" in wep[6]:
            focused = False
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
            if type(wep[6]["rapid_fire"]) is int:
                shots += (wep[6]["rapid_fire"])*wep[0]
            else:
                if len(wep[6]["rapid_fire"].split("+"))>1:
                    shoots = wep[6]["rapid_fire"].split("+")[0]
                    ex = int(wep[6]["rapid_fire"].split("+")[1])
                else:
                    shoots = wep[6]["rapid_fire"]
                    ex = 0
                if len(shoots.split("d")[0]) == 0:
                    for i in range(0, wep[0]):
                        shots += random.randint(1, int(shoots.split("d")[1]))+ex
                else:
                    for i in range(0, wep[0]*int(shoots.split("d")[0])):
                        shots += random.randint(1, int(shoots.split("d")[1]))+ex

        if verbose:
            print(f"nonblast attacks: {shots}")

        if "blast" in wep[6]:
            if len(target.melee_weapons10) == 0:
                for i in range (4, target.models, 5):
                    shots += wep[6]["blast"]*wep[0]
            else:
                for i in range (4, target.models *2, 5):
                    shots += wep[6]["blast"]*wep[0]

        if verbose:
            print(f"Total attacks: {shots}")

        checks = 0

        if wep[2] == "torrent":
            if verbose:
                print("torrent hits automatically")
            hits = shots
        else:
            to_hit = wep[2]
            if "heavy" in wep[6]:
                to_hit = wep[2]-1
            if (melee is False and target.stealth == 1) or target.minushit is True:
                to_hit += 1
            if unit.name == "Bloodthirster" and melee:
                to_hit -= 1
            if to_hit <2:
                to_hit = 2

            if verbose:
                print(f"to_hit neeeded: {to_hit}")
            for i in range(0, shots):
                crit = False
                hit=random.randint(1,6)

                if verbose:
                    print(f"rolled {hit} to hit")

                if (hit == 1 and "reroll_h_1" in wep[6]) or (hit < to_hit and ("oath" in wep[6] or (("epic_h" in wep[6] or "epic_hw" in wep[6]) and "character" in target.kw))):
                    hit=random.randint(1,6)
                    if verbose:
                        print(f"rerolled into {hit}")

                if hit == 1 and "hazardous" in wep[6]:
                    checks += 1
                if hit >= unit.crit_h_on or (hit > 3 and "conversion" in wep[6]):
                    crit = True
                    if verbose:
                        print("crit")

                if hit >= to_hit or crit:
                    if crit and ("lethal_hits" in wep[6] or "crit(auto-wound)" in wep[6]):
                        if verbose:
                            if unit.fortyk:
                                print("lethal")
                            if unit.aos:
                                print("auto-wound")
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
                            print("2 hits")
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
            if "anti-vehicle" in wep[6] and "vehicle" in target.kw:
                to_wound = wep[6]["anti-vehicle"]
            if "anti-infantry" in wep[6] and "infantry" in target.kw:
                to_wound = wep[6]["anti-infantry"]
            if "anti-character" in wep[6] and "character" in target.kw:
                to_wound = wep[6]["anti-character"]
            if "anti-psyker" in wep[6] and "psyker" in target.kw:
                to_wound = wep[6]["anti-psyker"]
        if unit.aos:
            to_wound = wep[3]
            rend = wep[4]
            if "anti-infantry" in wep[6] and "infantry" in target.kw:
                rend += 1
            if "anti-hero" in wep[6] and "hero" in target.kw:
                rend += 1
            if "anti-monster" in wep[6] and "monster" in target.kw:
                rend += 1
            if "anti-cavalry" in wep[6] and "cavalry" in target.kw:
                rend += 1
            if "anti-wizard" in wep[6] and "wizard" in target.kw:
                rend += 1
            if "anti-priest" in wep[6] and "priest" in target.kw:
                rend += 1
            if "anti-beast" in wep[6] and "beast" in target.kw:
                rend += 1
            if "anti-war_machine" in wep[6] and "war_machine" in target.kw:
                rend += 1
            if "anti-manifestation" in wep[6] and "manifestation" in target.kw:
                rend += 1

        if "lance" in wep[6]:
            if verbose:
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
            if wound<to_wound and ("twin-linked" in wep[6] or (("epic_w" in wep[6] or "epic_hw" in wep[6]) and "character" in target.kw)):
                wound = random.randint(1,6)
                if verbose:
                    print(f"rerolled into: {wound}")
            if wound >= to_wound:

                if verbose:
                    if wound >= unit.crit_w_on:
                        print("crit")
                    else:
                        print("wound")

                if wound >= unit.crit_w_on and "devastating_wounds" in wep[6]:
                    mortals = damage(wep[5], verbose = verbose)
                    if "melta" in wep[6]:
                        mortals += wep[6]["melta"]
                    if verbose:
                        print(f"devastating wound: {mortals} damage")

                    dmg = 0
                    if "psychic" in wep[6] and target.fnpp<target.fnpm:
                        dmg = libi_buff(target, mortals, verbose = verbose)
                    elif target.fnpm < 7:
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
        if unit.fortyk:
            to_save = target.save+wep[4]
            if "GKtermobuff" in wep[6] and "monster" not in target.kw and "vehicle" not in target.kw:
                to_save += 1
        if unit.aos:
            to_save = target.save+rend
        if melee is False and target.cover == 1 and "ignore_cover" not in wep[6]:
            if wep[4] > 0:
                to_save -= 1
                if verbose:
                    print("cover bonus")
            else:
                if target.save > 3:
                    to_save -= 1
                    if verbose:
                        print("cover bonus")
        if to_save < 2:
            to_save = 2

        if verbose:
            print(f"total wounds: {wounds}\n====================================")
            print(f"to_save needed: {to_save}")
            if target.invul < 7:
                print(f"invunerable save: {target.invul}")

        for i in range(0, wounds):
            save = random.randint(1,6)
            if verbose:
                print(f"save rolled: {save}")
                if save<to_save and save >= target.invul:
                    print("ivuln!")
            if save < to_save and save < target.invul:
                dmag = damage(wep[5], verbose = verbose)
                if "melta" in wep[6]:
                    dmag += wep[6]["melta"]
                if verbose:
                    print(f"damage dealt: {dmag}")

                if "psychic" in wep[6] and target.fnpp<target.fnp:
                    dmg = libi_buff(target, dmag, verbose = verbose)
                elif target.fnpm < 7:
                    dmg = 0
                    for i in range (dmag):
                        fnp1 = random.randint(1,6)
                        if verbose:
                            print(f"feel no pain: {fnp1}")
                        if fnp1 < target.fnp:
                            dmg += 1
                else:
                    dmg = dmag

                x,y,z = deal_damage(unit, target, dmg, x,y,z,verbose = verbose)

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
        if "focused" in wep[6]:
            focused = True

        if verbose:
            print("")

    if len(unit.weapons) == 0:
        temp = unit.hp
        dead = 0

    return x,y,z,strike,focused,unit.hp-temp,dead

def repeat_with_sweep(unit,target, x=0, y=0, z=0, xx= 0, yy = 0, zz = 0,allin = False, hazards = None, dead = None, verbose = False):
    if y == 0:
        y = target.hp
    if yy == 0:
        yy = target.hp

    for item in unit.weapons:
        if "strike" in item[6]:
            item[0] = 0
        if "sweep" in item[6]:
            item[0] = unit.models
    xx,yy,zz,strike, focused,hazards, dead = do_it(unit, target,xx,yy,zz,melee=True,strike=True, hazards = hazards, dead = dead, verbose = verbose)
    print(f"{unit.models} man {unit.name} deals {xx} damage to {target.name} using Sweep \n killing {zz} models.")
    report_hazards(unit, hazards, dead, verbose = verbose)

    for item in unit.weapons:
        if "strike" in item[6]:
            item[0] = unit.models
        if "sweep" in item[6]:
            item[0] = 0
    return False, xx,yy,zz,hazards, dead

def repeat_unfocused(unit, target, xx=0, yy=0, zz=0, hazards1 = 0, dead1=0,verbose = False):
    if yy == 0:
        yy = target.hp

    for item in unit.weapons:
        if "focused" in item[6]:
            item[0] = 0
        if "not" in item[6]:
            item[0] = unit.models

    xx,yy,zz,strike,focused,hazards1, dead1 = do_it(unit, target,xx,yy,zz,melee=False,strike=False,focused = True, hazards = hazards1, dead = dead1, verbose = verbose)
    print(f"{unit.models} man {unit.name} deals {xx} damage to {target.name} using unfocused shooting\n killing {zz} models")
    report_hazards(unit, hazards1, dead1, verbose = verbose)

    for item in unit.weapons:
        if "focused" in item[6]:
            item[0] = unit.models
        if "not" in item[6]:
            item[0] = 0

    return xx, yy, zz,hazards1,dead1

def shoot(unit, target, x=0, y=0, z=0, xx=0, yy=0, zz= 0,hazards = 0, dead = 0, verbose = False):
    if y == 0:
        y=target.hp
    if yy == 0:
        yy=target.hp

    print("Shooting:")

    if unit.ranged_weapons5 == []:
        print("No shooting here\n")
        return x,y,z,xx,yy,zz, hazards, dead

    unit.weapons = unit.ranged_weapons5

    x,y,z,strike,focused, hazards, dead = do_it(unit,target,x,y,z, verbose = verbose)

    hazards1,dead1 = 0,0

    if focused is False:
        print(f"{unit.models} man {unit.name} deals {x} damage to {target.name}\n killing {z} models")
        report_hazards(unit, hazards, dead, verbose = verbose)
    else:
        print(f"{unit.models} man {unit.name} deals {x} damage to {target.name} using focused shooting\n killing {z} models")
        report_hazards(unit, hazards, dead, verbose = verbose)
        xx, yy, zz,hazards1,dead1 = repeat_unfocused(unit, target, verbose = verbose)

    if unit.models != 1 and unit.ranged_weapons10 != []:

        unit.weapons = unit.ranged_weapons10
        x,y,z,strike,focused,hazards,dead = do_it(unit,target,x,y,z,hazards = hazards, dead = dead, verbose = verbose)

        if focused is False:
            print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name}\n killing {z} models")
            report_hazards(unit, hazards, dead, verbose = verbose)
        else:
            print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name} using focused shooting\n killing {z} models")
            report_hazards(unit, hazards, dead, verbose = verbose)
            xx, yy, zz,hazards1,dead1 = repeat_unfocused(unit, target, hazards1 = hazards1, dead1 = dead1, verbose = verbose)

    if hazards1 > hazards:
        hazards = hazards1
    if dead1 > dead:
        dead = dead1

    return x,y,z, xx,yy,zz, hazards, dead

def melee(unit, target, x=0, y=0, z=0, xx=0, yy = 0, zz = 0, allin = False,hazards = None, dead = None, verbose = False):
    if allin is False:
        x=0
        y=target.hp
        z=0
        xx = 0
        yy = target.hp
        zz = 0
    if y == 0:
        y = target.hp
    if yy == 0:
        yy = target.hp

    print("Melee combat:")

    unit.weapons = unit.melee_weapons5

    x,y,z,strike,focused,hazards,dead = do_it(unit,target,x,y,z, melee=True,hazards = hazards, dead = dead, verbose = verbose)

    if strike is False:
        print(f"{unit.models} man {unit.name} deals {x} damage to {target.name}\n killing {z} models.")
        report_hazards(unit, hazards, dead, verbose = verbose)
    else:
        print(f"{unit.models} man {unit.name} deals {x} damage to {target.name} using Strike \n killing {z} models.")
        report_hazards(unit, hazards, dead, verbose = verbose)
        strike, xx, yy, zz,hazards,dead = repeat_with_sweep(unit, target, x,y,z,xx, yy, zz, allin = allin,hazards = hazards, dead = dead, verbose = verbose)

    if (unit.models != 1 or unit.name == "Beast of Nurgle") and unit.melee_weapons10 != []:

        unit.weapons = unit.melee_weapons10
        x,y,z,strike,focused,hazards, dead = do_it(unit,target,x,y,z,melee=True, hazards = hazards, dead = dead,verbose = verbose)

        if strike is False:
            print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name}\n killing {z} models")
            report_hazards(unit, hazards, dead, verbose = verbose)
        else:
            print(f"{unit.models*2} man {unit.name} deals {x} damage to {target.name} using Strike\n killing {z} models")
            report_hazards(unit, hazards, dead, verbose = verbose)
            strike, xx, yy, zz,hazards, dead = repeat_with_sweep(unit, target, allin=allin, hazards = hazards, dead = dead,verbose = verbose)
    print("")

def all_in(unit, target, verbose=False):
    print(f"{unit.name} goes all-in on {target.name}:")
    x = 0
    y = 0
    z = 0
    x, y, z,xx,yy,zz,hazards, dead = shoot(unit, target, verbose = verbose)

    if zz>z:
        x += xx-x
        y += yy-y
        z += zz-z
    elif z>zz:
        xx += x-xx
        yy += y-yy
        zz += z-zz
    elif xx>x:
        x += xx-x
        y += yy-y
        z += zz-z
    elif x>xx:
        xx += x-xx
        yy += y-yy
        zz += z-zz


    if target.name == "Beast of Nurgle":
        y = target.hp
        yy = target.hp

    melee(unit, target, x, y, z, xx, yy, zz, allin = True,hazards = hazards, dead = dead, verbose = verbose)
