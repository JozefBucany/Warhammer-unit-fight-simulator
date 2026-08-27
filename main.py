import attack
from armies import daemons, gk, khorne, nurgle, slaanesh, tzeentch


def main():

    a= gk.StrikeSquad(["incinerator"],["incinerator"], cover = True, stealth = True)
    b= gk.Purifiers(["psycannon", "psycannon"], ["psycannon", "psycannon"], cover = False, crowe = True)
    c= gk.Interceptors(["psilencer"], ["psilencer"])
    d= gk.Purgators(["incinerator","psilencer", "psycannon", "incinerator"])
    x = gk.Terminator (["psycannon"], ["psycannon"],apothecary = True,libi = True)
    y = gk.Paladin (["incinerator","incinerator"], ["incinerator","incinerator"], ancient_weapon = ["incinerator"],apothecary = True, cover = True, stealth = True, voldus = True)
    n = gk.NDK("sword", ["psycannon", "psilencer"])
    gmndk = gk.GMNDK("mace", ["incinerator", "sublimator"])


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

    bc = gk.Brotherhood_Champion()
    cc = gk.Castellan_Crowe()
    tech = gk.Techmarine()

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

    brocap = gk.Brother_Captain(captain = True)
    libi = gk.Librarian(["combi-weapon"], libi = True)
    gm = gk.Grandmaster(["psycannon"])
    gmv = gk.GM_Voldus(voldus = True)
    chap = gk.Chaplain()

    print(brocap)
    attack.all_in(brocap,libi)
    print(libi)
    attack.all_in(libi,gm,verbose = False)
    print(gm)
    attack.all_in(gm, gmv)
    print(gmv)
    attack.all_in(gmv,chap)
    print(chap)
    attack.all_in(chap, brocap)


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
    attack.all_in(sg, sg,verbose = False)


if __name__ == "__main__":
    main()
