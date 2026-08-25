import attack
from armies import slaanesh

"""
from armies import GK
from armies import khorne
from armies import NDK
"""
"""
===========================================================
40k weapon abilities:

units count as not moving and in "good" spots, so:
- ASSAULT ignored
- RAPID FIRE always active
- CONVERSION always active
- HEAVY always active
- MELTA always active
- LANCE always active, units count as if charged (same as GK paladins with +1dmg on charge have their weapon characteristic permanently increased)
- abilities that work differently when "on objective" and such are always treated for better result (i.e. GK purifiers reroll ones, but reroll all wounds instead if attacking unit on an objective, so this program just gives them twin-linked and we call it done ;) )

BLAST always counts double the base amount of target models
EXTRA ATTACKS implemented during unit creation, all weapons added to list
FIRING DECK not used yet, but in future datasheets will be able to add desired infantry weapons during TRANSPORT creation
ONESHOT ignored, weapons always fire (meaning there is no oneshot check in the code, so dont even define it)
PISTOL ignored (as all shooting is done outside of combat,user sohuld add them only if able to fire them in regular shooting. i.e. unit with 24" rapid fire weapons would nver shoot with 12" pistol)
PRECISION ignored, units are led just for attacks and buff purposes
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
===========================================================
AOS weapon abilities:

charge(+1 dmg) - always on, units are considered to have charged
companion - ignored, no aura/leader buffs used in aos combat
shoot in combat - ignored, all shooting is considered to be out of combat

anti-x(+1 rend) - working (note that anti-charge is ignored as we consider attacking units to charge)
crit(2 hits) - working
crit(auto-wound) - working
crit(mortal) - working

AOS CODE IMPLEMENTATION STARTED, BUT NO TESTS WERE MADE YET, USE AT YOUR OWN RISK
===========================================================
"""

def main():
    """
    a= GK.StrikeSquad(["incinerator"],["incinerator"], cover = True, stealth = True)
    b= GK.Purifiers(["psycannon", "psycannon"], ["psycannon", "psycannon"], cover = False, crowe = True)
    c= GK.Interceptors(["psilencer"], ["psilencer"])
    d= GK.Purgators(["incinerator","psilencer", "psycannon", "incinerator"])
    x = GK.Terminator (["psycannon"], ["psycannon"],apothecary = True,libi = True)
    y = GK.Paladin (["incinerator","incinerator"], ["incinerator","incinerator"], ancient_weapon = ["incinerator"],apothecary = True, cover = True, stealth = True, voldus = True)
    n = NDK.NDK("sword", ["psycannon", "psilencer"])
    gmndk = NDK.GMNDK("mace", ["incinerator", "sublimator"])

    print(a)
    print(b)
    attack.shoot(a,b)
    attack.melee(a,b)
    attack.shoot(b,a)
    attack.melee(b,a)
    print(c)
    print(d)
    attack.shoot(c,d)
    attack.melee(c,d)
    attack.shoot(d,c)
    attack.melee(d,c)
    print(x)
    print(y)
    attack.shoot(x,y)
    attack.melee(x,y)
    attack.shoot(y,x)
    attack.melee(y,x)
    print(n)
    attack.shoot(n,d)
    attack.melee(n,d)

    bc = GK.Brotherhood_Champion()
    cc = GK.Castellan_Crowe()
    tech = GK.Techmarine()

    print(bc)
    attack.shoot(bc,d)
    attack.melee(bc,d)
    print(cc)
    attack.shoot(cc,d)
    attack.melee(cc,d)
    print(tech)
    attack.shoot(tech,d)
    attack.melee(tech,d)
    attack.all_in(n,d)
    print(gmndk)
    attack.shoot(gmndk,d)
    attack.melee(gmndk,d)
    attack.all_in(gmndk,d)

    brocap = GK.Brother_Captain(captain = True)
    libi = GK.Librarian(["combi-weapon"], libi = True)
    gm = GK.Grandmaster(["psycannon"])
    gmv = GK.GM_Voldus(voldus = True)
    chap = GK.Chaplain()

    print(brocap)
    attack.all_in(brocap,libi)
    print(libi)
    attack.all_in(libi,gm)
    print(gm)
    attack.all_in(gm, gmv)
    print(gmv)
    attack.all_in(gmv,chap)
    print(chap)
    attack.all_in(chap, brocap)

    test_unit = GK.TestUnit(captain = False)
    print(test_unit)
    attack.all_in(test_unit, d)
    attack.all_in(test_unit, a)
    attack.all_in(test_unit, x)
    attack.all_in(test_unit, y)
    attack.all_in(test_unit, n)

    bloodletters = khorne.Bloodletters40k(blmas=True)
    print(bloodletters)
    attack.all_in(bloodletters,bloodletters)

    flesh_hounds = khorne.Flesh_Hounds40k()
    print(flesh_hounds)
    attack.all_in(flesh_hounds,bloodletters)

    blood_crushers = khorne.Blood_Crushers40k(skmas = True)
    print(blood_crushers)
    attack.all_in(blood_crushers,bloodletters)

    skull_cannon = khorne.Skull_Cannon40k()
    print(skull_cannon)
    attack.all_in(skull_cannon,bloodletters)

    bm = khorne.Bloodmaster40k()
    print(bm)
    attack.all_in(bm,bloodletters)

    kar = khorne.Karanak40k()
    print(kar)
    attack.all_in(kar,bloodletters)

    skm = khorne.Skullmaster40k()
    print(skm)
    attack.all_in(skm, bloodletters)

    skt = khorne.Skulltaker40k()
    print(skt)
    attack.all_in(skt,bloodletters)

    skar = khorne.Skarbrand40k()
    print(skar)
    attack.all_in(skar,bloodletters)

    bt = khorne.Bloodthirster40k("axe+breath")
    bt2 = khorne.Bloodthirster40k("lash+flail")
    print(bt)
    attack.all_in(bt, bloodletters)
    print(bt2)
    attack.all_in(bt2, bloodletters)
    """

    daemonettes = slaanesh.Daemonettes40k(epitome = True)
    print(daemonettes)
    attack.all_in(daemonettes,daemonettes, verbose = True)

    daemonettes2 = slaanesh.Daemonettes40k(syll = True)
    print(daemonettes2)
    attack.all_in(daemonettes2,daemonettes, verbose = True)

    daemonettes3 = slaanesh.Daemonettes40k(trance = True)
    print(daemonettes3)
    attack.all_in(daemonettes3,daemonettes, verbose = True)

    fiends = slaanesh.Fiends40k()
    print(fiends)
    attack.all_in(fiends,daemonettes)

    seekers = slaanesh.Seekers40k()
    print(seekers)
    attack.all_in(seekers,daemonettes)

    hellflayer = slaanesh.Hellflayer40k()
    print(hellflayer)
    attack.all_in(hellflayer,daemonettes)

    trance = slaanesh.TranceWeaver40k(trance = True)
    print(trance)
    attack.all_in(trance,daemonettes,verbose = True)

    epitome = slaanesh.Epitome40k(epitome = True)
    print(epitome)
    attack.all_in(epitome,daemonettes, verbose = True)

    enrapt = slaanesh.Enrapturess40k()
    print(enrapt)
    attack.all_in(enrapt,daemonettes, verbose = True)

    sylleske = slaanesh.Syllesske40k(syll = True)
    print(sylleske)
    attack.all_in(sylleske,daemonettes, verbose = True)

    keeper = slaanesh.Keeper40k("shield")
    print(keeper)
    attack.all_in(keeper,daemonettes, verbose = True)

    shalaxi = slaanesh.Shalaxi40k()
    print(shalaxi)
    attack.all_in(shalaxi,daemonettes, verbose = True)


    #Implement FOCUSED /"not" with 0 models
    #implement full reroll to hit
    #implement crit wound on 5+
    return

if __name__ == "__main__":
    main()
