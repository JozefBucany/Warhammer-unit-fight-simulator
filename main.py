from armies.gk import Interceptors, Paladin, Purgators, Purifiers, StrikeSquad, Terminator
from armies.NDK import NDK


def main():
    a= StrikeSquad("incinerator",True)
    b= Purifiers("psycannon")
    c= Interceptors("psilencer")
    d= Purgators("incinerator")
    x = Terminator ("psycannon")
    y = Paladin ("incinerator")
    n = NDK("sword", "psycannon", "incinerator")

    print(a)
    print("")
    print(b)
    print("")
    a.shoot(b)
    a.melee(b)
    b.shoot(a)
    b.melee(a)
    print("")
    print(c)
    print("")
    print(d)
    print("")
    c.shoot(d)
    c.melee(d)
    print("")
    print(x)
    print("")
    print(y)
    print("")
    x.shoot(y)
    x.melee(y)
    print("")
    print(n)
    n.shoot(d)
    n.melee(c)

    return

main()
