from code import interact

from armies.GK import (
    Brother_Captain,
    Brotherhood_Champion,
    Castellan_Crowe,
    Chaplain,
    GM_Voldus,
    Grandmaster,
    Interceptors,
    Librarian,
    Paladin,
    Purgators,
    Purifiers,
    StrikeSquad,
    Techmarine,
    Terminator,
)
from armies.NDK import GMNDK, NDK
from attack import all_in, melee, shoot

"""

40k weapon abilities:

units count as not moving and in "good" spots, so:
- ASSAULT ignored
- RAPID FIRE always active
- CONVERSION always active
- HEAVY always active
- MELTA always active
- LANCE always active, units count as if charged

BLAST always counts double the base amount of target models
EXTRA ATTACKS implemented during unit creation, all weapons added to list
FIRING DECK not used yet, but in future datasheets will be able to add desired infantry weapons during TRANSPORT creation
ONESHOT ignored, weapons always fire (meaning there is no oneshot check in the code, so dont even define it)
PISTOL ignored (as all shooting is done outside of combat,user sohuld add them only if able to fire them in regular shooting. i.e. unit with 24" rapid fire weapons would nver shoot with 12" pistol)
PRECISION ignored, units are led just for buff purposes
INDIRECT ignored, target always treated as visible

ANTI-X checks working
CRIT HITS and CRIT WOUNDS working
DEVASTATING wounds working
FEEL NO PAIN working
HAZARDOUS working
IGNORE COVER working, cover defined during unit creation
LETHAL HITS working
STEALTH working, defined during unit creation
SUSTAINED HITS working
TORRENT working
TWIN-LINKED working

==================WIP ===================
feel no pain against psychic attacks
==================WIP ===================


AOS weapon abilities:

charge(+1 dmg) - always on, units are considered to have charged
companion - ignored, no aura/leader buffs used in aos combat
shoot in combat - ignored, all shooting is considered to be out of combat

anti-x(+1 rend) - working (note that anti-charge is ignored as we consider attacking units to charge)
crit(2 hits) - working
crit(auto-wound) - working
crit(mortal) - working
"""

def main():

    a= StrikeSquad(["incinerator"],["incinerator"], cover = True, stealth = False)
    b= Purifiers(["psycannon", "psycannon"], ["psycannon", "psycannon"], cover = False, crowe = True)
    c= Interceptors(["psilencer"], ["psilencer"])
    d= Purgators(["incinerator","incinerator", "incinerator", "incinerator"])
    x = Terminator (["psycannon"], ["psycannon"],apothecary = True)
    y = Paladin (["incinerator","incinerator"], ["incinerator","incinerator"], ancient_weapon = ["incinerator"],apothecary = True)
    n = NDK("sword", ["psycannon", "psilencer"])
    gmndk = GMNDK("mace", ["incinerator", "sublimator"])
    bc = Brotherhood_Champion()
    cc = Castellan_Crowe()
    tech = Techmarine()

    print(a)
    print(b)
    shoot(a,b)
    melee(a,b)
    shoot(b,a)
    melee(b,a)
    print(c)
    print(d)
    shoot(c,d)
    melee(c,d)
    shoot(d,c)
    melee(d,c)
    print(x)
    print(y)
    shoot(x,y)
    melee(x,y)
    shoot(y,x)
    melee(y,x)
    print(n)
    shoot(n,d)
    melee(n,d)


    print(bc)
    shoot(bc,d)
    melee(bc,d)
    print(cc)
    shoot(cc,d)
    melee(cc,d)
    print(tech)
    shoot(tech,d)
    melee(tech,d)
    all_in(n,d)
    print(gmndk)
    shoot(gmndk,d)
    melee(gmndk,d)
    all_in(gmndk,d, verbose=True)

    brocap = Brother_Captain(captain = True)
    libi = Librarian(["combi-weapon"], libi = True)
    gm = Grandmaster(["psycannon"])
    gmv = GM_Voldus(voldus = True)
    chap = Chaplain()

    print(brocap)
    print(libi)
    print(gm)
    print(gmv)
    print(chap)

    all_in(brocap,libi, verbose=True)
    all_in(libi,gm, verbose=True)
    all_in(gm, gmv, verbose=True)
    all_in(gmv,chap, verbose=True)
    all_in(chap, brocap, verbose=True)


if __name__ == "__main__":
    main()
