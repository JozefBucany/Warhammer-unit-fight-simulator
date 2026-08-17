from armies.gk import (
    Interceptors,
    Paladin,
    Purgators,
    Purifiers,
    StrikeSquad,
    Terminator,
)
from func.attack import attack


def main():
    a= StrikeSquad("stormbolter")
    b= Purifiers("psycannon")
    c= Interceptors("psilencer")
    d= Purgators("incinerator")
    x = Paladin ("incinerator")
    y = Terminator ("psycannon")


    print(f"{a}\n")
    print(f"{b}\n")
    print(f"{c}\n")
    print(f"{d}\n")
    print(f"{x}\n")
    print(f"{y}\n")


    attack(a,b)


main()
