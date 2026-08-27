**Welcome** to Warhammer Battle Simulator.

You probably know resources, which can tell you how much damage can you expect from an unit on average. That's why i made this as
**My first python project on boot.dev learning site.**
This program takes 2 of my favorite armies to take the heck out of each other in a totally random environment. all rolls, all checks, are done by "random" module and no "averages" are considered here.


**Basics**

Basic units are created from data by Games Workshop, all IP rights belong to them, this is just a fan project and i`m not selling this to anyone.

What you might want to know is that there is no interface yet and all inputs are done via editing main.py main function. FOR NOW. (i just need to stop with this project for a bit and focus on different things)

For this program to run you don't need any special modules or downloads (for now).

**What you can find in this project**

I found a way to implement most 40k weapons and abilities used in Grey Knights and Daemons armies. Some lines of code are prepared for more armies to come, when i remembered something may be useful and easy to implement, i added it in even if these armies are not using it yet.

All units (where possible) have their datasheet abilities implemented somehow (more on that later) if those abilities are "once per battle", such as Daemon prices' abilities, they ARE active

Units count as not having moved and in "good" spots, so:
- ASSAULT ignored
- RAPID FIRE always active
- CONVERSION always active
- HEAVY always active
- MELTA always active
- LANCE always active, all units count as having charged

- BLAST always counts maximum amount of target models (i.e. GK strike squad = 10, same as Bloodletters = 10)
- EXTRA ATTACKS implemented during unit creation, all weapons are added to list and attacked with
- FIRING DECK not used yet, but in future datasheets  will be able to add desired infantry weapons during TRANSPORT creation
- ONESHOT ignored, weapons always fire
- PISTOL ignored (as all shooting is done outside of combat, pistol weapons are defined only if it's the only weapon, or can be used. i.e. unit with 24" rapid fire weapons would never shoot with 12" pistol)
- PRECISION ignored, units are led just for attacks and buff purposes. That said,if LEADER is attached to a unit, their attacks are added to the unit's weapons lists and, where possible, their LADER abilities are activated (looking at you, Exalted Flamer)
- i made some LEADERs able to lead themselves for testing purposes, keeping this feature in the code, use freely if desired (weapons are not duplicated in the process)
- INDIRECT ignored, targets always treated as visible
- aura abilities on some characters, such as Lord of Change, are always active on themselves (uits have their abilities or weapons characteristics adjusted to represent this)
- weapons with multiple choices are marked with strike/sweep for melee and focused/not for shooting.
    * during melee and shoot attacks results are calculated and printed separately.
    * during all_in attack: shooting is printed as if shoot was used, but then higher casualties/higher damage shooting result is chosen to overflow into melee (normal attacs, strike and sweep all calculate with this better shooting result)

- ANTI-X checks working
- CRIT HITS and CRIT WOUNDS working
- DEVASTATING wounds working
- FEEL NO PAIN working (all 3 versions should work properly. regular fnp, fnp against psychic attacks and fnp against mortals)
- HAZARDOUS working and reported after attacks
- IGNORE COVER working (cover defined during unit creation)
- LETHAL HITS working
- STEALTH working, defined during unit creation
- SUSTAINED HITS working
- TORRENT working
- TWIN-LINKED working

!!!
Note that many abilities were too hard (or useless) to code (cough... beast of nurgle... cough), so where there is no direct representation of these abilities behaviour, i took liberty of doing hard coded stuff (again, beast) or used aos abilities (i.e. GK paladins charge +1 dmg)
i also decided that abilities that work differently when "on objective" and such are always treated for better result (i.e. GK purifiers reroll ones, but reroll all wounds instead ff attacking unit on an objective, so I just gave them twin-linked and call it done ;) )
!!!


!!! if you want to define your own units, be careful with strike a focused weapons (frag/krak in future as well).
!!! ordering of MULTIPLE weapons of these types matter. if you define Strike-weapon 1 before Strike weapon 2,
!!! sweep 1 needs to come before sweep2. Even if code works without errors, your values may get messed up
!!! during attack, because of how strike/sweep and focused/not interaction is coded.

=========================================================

**AOS weapon abilities:**

I implemented few checks for AoS support, although not fully implemented yet.

- charge(+1 dmg) - always on, units are considered to have charged
- companion - ignored, no aura/leader buffs used in aos combat (except units benefiting from their own buffs)
- shoot in combat - ignored, all shooting is considered to be out of combat
- anti-x(+1 rend) - working (note that anti-charge is ignored as we consider attacking units to charge)
- crit(2 hits) - working
- crit(auto-wound) - working
- crit(mortal) - working

AOS CODE IMPLEMENTATION STARTED, BUT NO TESTS WERE MADE YET, USE AT YOUR OWN RISK

=========================================================

**HOW TO USE**

Code can be launched by running python3 main.py, but is highly suggested to edit main.py before first start, as there is **A LOT** of units there for testing purposes and results in printing a wall of text to the terminal

and now, how to use the code, if you are still interested:
first you need to create a unit from a predefined class in armies folder

`strike_squad = gk.StrikeSquad()`

If you wish to add a special weapon to the unit, use lists for addind weapon to a 5 man group and 10 man group.

`strike_squad = gk.StrikeSquad(["psycannon"],["psilencer"])`

This creates a unit of 5 models with 1 psycannon and additional 5 models with 1 psilencer
Different armies have different rules, so best way to figure out how to create an unit with special weapons, see the code itself. (in future, with more armies, i will describe how units work at the top of the army file itself)
We need to use list even for one weapon, because strike squad is based on same code as other units to reduce duplicity, and others are able to equip more than 1 special weapon.
i.e. Purifiers would be declared as 

`gk.Purifiers(["psycannon", "psycannon"], ["psycannon", "psycannon"], crowe = True)`

Next, if the unit expects you to shoot at it, it may take cover by addind cover = True after the weapon lists, of even get stealth = True, for additional defensiveness.

`strike_squad = gk.StrikeSquad(["psycannon"],["psilencer"],cover = True, stealth = True)`

Lastly, some units can be attached to a LEADER character. you do this by adding his argument (see armies for different arguments of different leaders) to the end...

`strike_squad = gk.StrikeSquad(["psycannon"],["psilencer"],cover = True, stealth = True, tech = True)`

This adds techmarine to the strike squad to lead them. (he has no usable leader ability, but his melee and ranged weapons will be added to the weapons list and when the unit attacks, techmarine will attack with them).

Now that we have our unit created, let's get them something to charge to

`bloodletters = khorne.Bloodletters40k()`

... creates Khorne Bloodletters unit with 10 models. as they have no special weapons to choose from, we can maybe give them a leader.

`bloodletters = khorne.Bloodletters40k(blmas = True)`

adds Blood Master to lead them (during report of killed models after attacking, leaders not considered yet)

Now we have out 2 units, we can start fighting.
Attack abilities are defined in an imported attack.py file. we can shoot, melee, or all_in our targets.
syntax is simple and same for all

`attack.shoot(strike_squad, bloodletters)`

shoots all ranged weapons in strike squad at bloodletters and they try to save themselves, using all abilities and/or buffs they might have. at the end, report is made of how much damage we were abe to deal and how many models died.

`attack.melee(strike_squad, bloodletters)`

does the same, but unit charges and attacks with melee weapons.
and if we really REALLY want them dead, we can

`attack.all_in(strike_squad, bloodletters)`

this will shoot at them, remember amount od damage and casualties, and charge into melee fight straight after the shooting, reporting total amount of damage and dead models.

Remember! in Warhammer 40k, additional damage after killing a model is lost, so attacking 1 healt bloodletters with 2 damage weapon still kills just 1 model, so more often than not, you may see stuff like "dealt 12 damage, 2 models die"

lastly, we have an option to make the resulting printout more detailed. you can see every roll, every resulting hit or devastating wound yourself by adding verbose to the attacking function
`attack.all_in(strike_squad, bloodletters, verbose = True)`
This makes a HUGE amount of text appear on the screen, so be careful to not overdo it (during testing i gave 800 attacks to a single model and let him go for it... in an online interpreter... my internet browser was not happy)

That is all for now, so if you enjoy, feel free to keep it and keep working on it yourself. i`ll return to it and keep adding stuff later.

Thanks
