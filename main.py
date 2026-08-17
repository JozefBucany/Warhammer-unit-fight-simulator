from armies.gk import (
    Interceptors,
    Paladin,
    Purgators,
    Purifiers,
    StrikeSquad,
    Terminator,
)
from func.attack import melee, shoot


def main():
    a= StrikeSquad("stormbolter")
    b= Purifiers("psycannon")
    c= Interceptors("psilencer")
    d= Purgators("incinerator")
    x = Paladin ("incinerator")
    y = Terminator ("psycannon")


    print(a)
    print("")
    print(b)
    print("")
    print(c)
    print("")
    print(d)
    print("")
    print(x)
    print("")
    print(y)
    print("")


    shoot(a,b)
    melee(a,b)



    return

main()
