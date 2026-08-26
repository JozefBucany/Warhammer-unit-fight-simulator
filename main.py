import attack
from armies import GK, NDK, daemons, khorne, nurgle, slaanesh, tzeentch

"""
===========================================================
40k weapons and abilities:

all units (where possible) have their dtasheet abilities implemented somehow (more on that later)
if those abilities are "once per battle", such as Daemon prices' abilities, they ARE active

units count as not having moved and in "good" spots, so:
- ASSAULT ignored
- RAPID FIRE always active
- CONVERSION always active
- HEAVY always active
- MELTA always active
- LANCE always active, all units count as having charged

BLAST always counts maximum amount of target models (i.e. GK strike squad = 10, same as Khorne Bloodletters = 10)
EXTRA ATTACKS implemented during unit creation, all weapons added to list
FIRING DECK not used yet, but in future datasheets will be able to add desired infantry weapons during TRANSPORT creation
ONESHOT ignored, weapons always fire
PISTOL ignored (as all shooting is done outside of combat, pistol weapons are defined only if it's the only
    weapon, or can be used. i.e. unit with 24" rapid fire weapons would never shoot with 12" pistol)
PRECISION ignored, units are led just for attacks and buff purposes
that said,if LEADER is attached to a unit, their attacks are added to the unit's weapons lists and, where possible,
    their LADER abilities are activated (looking at you, Exalted Flamer)
    - i made some LEADERs able to lead themselves for testing purposes, keeping this feature in the code,
        use freely if desired (weapons are not duplicated in the process)
INDIRECT ignored, targets always treated as visible
aura abilities on some characters, such as Lord of Change, are always active on themselves
    (uits have their abilities or weapons characteristics adjusted to represent this)
weapons with multiple choices are marked with strike/sweep for melee and focused/not for shooting.
    * during melee and shoot attacks results are calculated and printed separately.
    * during all_in attack: shooting is printed as if shoot was used, but then
        higher casualties/higher damage shooting result is chosen to overflow into melee
        (normal attacs, strike and sweep all calculate with this better shooting result)

ANTI-X checks working
CRIT HITS and CRIT WOUNDS working
DEVASTATING wounds working
FEEL NO PAIN working (all 3 versions should work properly.
    regular fnp, fnp against psychic attacks and fnp against mortals)
HAZARDOUS working and reported after attacks
IGNORE COVER working (cover defined during unit creation)
LETHAL HITS working
STEALTH working, defined during unit creation
SUSTAINED HITS working
TORRENT working
TWIN-LINKED working

!!!
    note that many abilities were too hard (or useless) to code (cough... beast of nurgle... cough),
so where there is no direct representation of these abilities behaviour, i took liberty of doing
hard coded stuff (again, beast) or used aos abilities (i.e. GK panadins charge +1 dmg)
    i also decided that abilities that work differently when "on objective" and such
are always treated for better result (i.e. GK purifiers reroll ones, but reroll all wounds
instead if attacking unit on an objective, so I just gave them twin-linked and call it done ;) )
!!!

===========================================================
AOS weapon abilities:

charge(+1 dmg) - always on, units are considered to have charged
companion - ignored, no aura/leader buffs used in aos combat
    (except units benefiting from their own buffs)
shoot in combat - ignored, all shooting is considered to be out of combat

anti-x(+1 rend) - working (note that anti-charge is ignored as we consider attacking units to charge)
crit(2 hits) - working
crit(auto-wound) - working
crit(mortal) - working

AOS CODE IMPLEMENTATION STARTED, BUT NO TESTS WERE MADE YET, USE AT YOUR OWN RISK
===========================================================
"""

def main():

    a= GK.StrikeSquad(["incinerator"],["incinerator"], cover = True, stealth = True)
    b= GK.Purifiers(["psycannon", "psycannon"], ["psycannon", "psycannon"], cover = False, crowe = True)
    c= GK.Interceptors(["psilencer"], ["psilencer"])
    d= GK.Purgators(["incinerator","psilencer", "psycannon", "incinerator"])
    x = GK.Terminator (["psycannon"], ["psycannon"],apothecary = True,libi = True)
    y = GK.Paladin (["incinerator","incinerator"], ["incinerator","incinerator"], ancient_weapon = ["incinerator"],apothecary = True, cover = True, stealth = True, voldus = True)
    n = NDK.NDK("sword", ["psycannon", "psilencer"])
    gmndk = NDK.GMNDK("mace", ["incinerator", "sublimator"])

    print(a)
    attack.shoot(a,b)
    attack.melee(a,b)
    print(b)
    attack.shoot(b,a)
    attack.melee(b,a)
    print(c)
    attack.shoot(c,d)
    attack.melee(c,d)
    print(d)
    attack.shoot(d,c)
    attack.melee(d,c)
    print(x)
    attack.shoot(x,y)
    attack.melee(x,y)
    print(y)
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
    attack.all_in(tech,d)
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


    daemonettes = slaanesh.Daemonettes40k(epitome = True)
    print(daemonettes)
    attack.all_in(daemonettes,daemonettes)

    daemonettes2 = slaanesh.Daemonettes40k(syll = True)
    print(daemonettes2)
    attack.all_in(daemonettes2,daemonettes)

    daemonettes3 = slaanesh.Daemonettes40k(trance = True)
    print(daemonettes3)
    attack.all_in(daemonettes3,daemonettes)

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
    attack.all_in(trance,daemonettes)

    epitome = slaanesh.Epitome40k(epitome = True)
    print(epitome)
    attack.all_in(epitome,daemonettes)

    enrapt = slaanesh.Enrapturess40k()
    print(enrapt)
    attack.all_in(enrapt,daemonettes)

    sylleske = slaanesh.Syllesske40k(syll = True)
    print(sylleske)
    attack.all_in(sylleske,daemonettes)

    keeper = slaanesh.Keeper40k("shield")
    print(keeper)
    attack.all_in(keeper,daemonettes)

    shalaxi = slaanesh.Shalaxi40k()
    print(shalaxi)
    attack.all_in(shalaxi,daemonettes)


    plaguebearers = nurgle.PlagueBearers40k()
    print(plaguebearers)
    attack.shoot(plaguebearers,plaguebearers,verbose = False)
    attack.melee(plaguebearers,plaguebearers,verbose = False)
    attack.all_in(plaguebearers,plaguebearers,verbose = False)

    plaguebearers2 = nurgle.PlagueBearers40k(spoil = True)
    print(plaguebearers2)
    attack.all_in(plaguebearers2,plaguebearers)

    plaguebearers3 = nurgle.PlagueBearers40k(pox = True)
    print(plaguebearers3)
    attack.all_in(plaguebearers3,plaguebearers)

    nurglings = nurgle.Nurglings40k()
    print(nurglings)
    attack.all_in(nurglings ,plaguebearers)

    drones = nurgle.Drones40k()
    print(drones)
    attack.all_in(drones,plaguebearers)

    beast = nurgle.Beast40k()
    print(beast)
    attack.shoot(beast,plaguebearers,verbose = False)
    attack.melee(beast,plaguebearers,verbose = False)
    attack.all_in(beast,plaguebearers,verbose = False)

    sloppity = nurgle.Sloppity40k()
    print(sloppity)
    attack.all_in(sloppity,plaguebearers)

    spoilpox = nurgle.Spoilpox40k(spoil = True)
    print(spoilpox)
    attack.all_in(spoilpox,plaguebearers)

    poxbringer = nurgle.Poxbringer40k(pox = True)
    print(poxbringer)
    attack.all_in(poxbringer,plaguebearers)

    horti = nurgle.Horti40k()
    print(horti)
    attack.all_in(horti,plaguebearers)

    guo1 = nurgle.GUO40k(["sword","flail"])
    print(guo1)
    attack.shoot(guo1,plaguebearers,verbose = False)
    attack.melee(guo1,plaguebearers,verbose = False)
    attack.all_in(guo1,plaguebearers,verbose = False)

    guo2 = nurgle.GUO40k(["bell","dagger"])
    print(guo2)
    attack.all_in(guo2,plaguebearers)

    rotigus = nurgle.Rotigus40k()
    print(rotigus)
    attack.all_in(rotigus,plaguebearers)

    phorrors = tzeentch.PHorrors40k(chan = True)
    print(phorrors)
    attack.shoot(phorrors,phorrors,verbose = False)
    attack.melee(phorrors,phorrors,verbose = False)
    attack.all_in(phorrors,phorrors)

    bb1horrors = tzeentch.BB1Horrors40k(flux = True)
    print(bb1horrors)
    attack.all_in(bb1horrors,phorrors)

    bb2horrors = tzeentch.BB2Horrors40k()
    print(bb2horrors)
    attack.all_in(bb2horrors,phorrors)

    flamers = tzeentch.Flamers40k(flam=True)
    print(flamers)
    attack.shoot(flamers,phorrors,verbose = False)
    attack.melee(flamers,phorrors,verbose = False)
    attack.all_in(flamers,phorrors)

    screamers = tzeentch.Screamers40k(fate = True)
    print(screamers)
    attack.shoot(screamers,phorrors,verbose = False)
    attack.melee(screamers,phorrors,verbose = False)
    attack.all_in(screamers,phorrors)


    chariot = tzeentch.Chariot40k()
    print(chariot)
    attack.shoot(chariot,phorrors,verbose = False)
    attack.melee(chariot,phorrors,verbose = False)
    attack.all_in(chariot,phorrors)

    change = tzeentch.Changecaster40k(chan = True)
    print(change)
    attack.all_in(change,phorrors)

    flux = tzeentch.Fluxmaster40k(flux = True)
    print(flux)
    attack.all_in(flux,phorrors)

    exa = tzeentch.Exaflam40k()
    print(exa)
    attack.all_in(exa,phorrors)

    fate = tzeentch.Fateskimmer40k(fate = True)
    print(fate)
    attack.all_in(fate,phorrors)

    loc = tzeentch.LoC40k("sword")
    print(loc)
    attack.all_in(loc,phorrors)

    loc = tzeentch.LoC40k("rod","sustain")
    print(loc)
    attack.all_in(loc,phorrors)

    loc = tzeentch.LoC40k("rod","lethal")
    print(loc)
    attack.all_in(loc,phorrors)

    loc = tzeentch.LoC40k("rod","ignore")
    print(loc)
    attack.all_in(loc,phorrors)

    kai = tzeentch.Kairos40k()
    print(kai)
    attack.all_in(kai,phorrors)

    bel = daemons.Belakor40k()
    print(bel)
    attack.shoot(bel,d)
    attack.melee(bel,fiends)
    attack.all_in(bel,sylleske, verbose = False)

    dp = daemons.DP40k("khorne")
    print(dp)
    attack.all_in(dp, d)

    dp = daemons.DP40k("nurgle")
    print(dp)
    attack.all_in(dp, d)

    dp = daemons.DP40k("slaanesh")
    print(dp)
    attack.all_in(dp, d)

    dp = daemons.DP40k("tzeentch")
    print(dp)
    attack.all_in(dp, d)

    dpw = daemons.DPW40k("khorne", "sustained")
    print(dpw)
    attack.all_in(dpw, d)

    dpw = daemons.DPW40k("nurgle", "lethal")
    print(dpw)
    attack.all_in(dpw, d)

    dpw = daemons.DPW40k("slaanesh","sustained")
    print(dpw)
    attack.all_in(dpw, d)

    dpw = daemons.DPW40k("tzeentch", "lethal")
    print(dpw)
    attack.all_in(dpw, d)

    sg = daemons.SoulGrinder40k("sword","khorne")
    print(sg)
    attack.all_in(sg, x)

    sg = daemons.SoulGrinder40k("sword","nurgle")
    print(sg)
    attack.all_in(sg, x)

    sg = daemons.SoulGrinder40k("claw","slaanesh")
    print(sg)
    attack.all_in(sg, x)

    sg = daemons.SoulGrinder40k("sword","tzeentch")
    print(sg)
    attack.all_in(sg, x)



if __name__ == "__main__":
    main()
