import random


class Inf_Weapon():
    def __init__(self, weapon: str, cover: bool = False):
        self.cover = 0
        if cover:
            self.cover = 1
        self.weapon = weapon
        self.apothecary = 0
        self.amount = 0
        self.amount_10 = 0
        self.default_shots = 2
        self.default_BS = 3
        self.default_ranged_str = 4
        self.default_ranged_ap = 0
        self.default_ranged_dmg = 1
        self.default_ranged_ability = "rapid_fire 2"
        match (weapon):
            case "psycannon":
                self.shots = 3
                self.BS = 3
                self.ranged_str = 8
                self.ranged_ap = 1
                self.ranged_dmg = 2
                self.ranged_ability = ""
            case "psilencer":
                self.shots = 6
                self.BS = 3
                self.ranged_str = 5
                self.ranged_ap = 0
                self.ranged_dmg = 1
                self.ranged_ability = "sustained_hits 1"
            case "incinerator":
                self.shots = "d6"
                self.BS = "torrent"
                self.ranged_str = 6
                self.ranged_ap = 1
                self.ranged_dmg = 1
                self.ranged_ability = "ignore cover"
            case _:
                self.shots = 2
                self.BS = 3
                self.ranged_str = 4
                self.ranged_ap = 0
                self.ranged_dmg = 1
                self.ranged_ability = "rapid_fire 2"

    def shoot(self, target):
        x = 0
        hits = 0
        wounds = 0

        if type(self.default_BS) is int:
            def_shots = self.default_shots
            if self.default_ranged_ability.split(" ")[0] == "rapid_fire":
                def_shots += int(self.default_ranged_ability.split(" ")[1])

        if type(self.BS) is int:
            spec_shots = self.shots
            if self.ranged_ability.split(" ")[0] == "rapid_fire":
                spec_shots += int(self.ranged_ability.split(" ")[1])

        #default weapon
        if type(self.default_BS) is int:
            for i in range(0, def_shots*(5-self.amount-self.apothecary)):
                hit=random.randint(1,6)
                if hit >= self.default_BS:
                    hits += 1
                    if hit == 6 and self.default_ranged_ability.split(" ")[0] == "sustained_hits":
                        extra = self.default_ranged_ability.split(" ")[1]
                        if extra[0] != "d":
                            extra = int(extra)
                        else:
                            extra = random.randint(1,int(extra[1]))
                        hits += extra
                    if hit == 6 and self.default_ranged_ability.split(" ")[0] == "lethal_hits":
                        hits -=1
                        wounds += 1
        else:
            for i in range(0, 5-self.amount-self.apothecary):
                hits += random.randint(1, int(self.default_shots[1]))

        if self.default_ranged_str == target.toughness:
            to_wound = 4
        if self.default_ranged_str > target.toughness:
            to_wound = 3
        if self.default_ranged_str < target.toughness:
            to_wound = 5
        if self.default_ranged_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.default_ranged_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1
                if self.default_ranged_ability.split(" ")[0] == "Devastating_wounds":
                    wounds -= 1
                    x += self.default_ranged_dmg

        for i in range(0, wounds):
            save = random.randint(1,6)
            to_save = target.save+self.default_ranged_ap
            if target.cover == 1 and self.default_ranged_ability != "ignore cover":
                if self.default_ranged_ap > 0:
                    to_save -= 1
                else:
                    if target.save > 3:
                        to_save -= 1
            if save < to_save and save < target.invul:
                x += self.default_ranged_dmg

        hits = 0
        wounds = 0

        #specials
        if type(self.BS) is int:
            for i in range(0, spec_shots*self.amount):
                hit=random.randint(1,6)
                if hit >= self.BS:
                    hits += 1
                    if hit == 6 and self.ranged_ability.split(" ")[0] == "sustained_hits":
                        extra = self.ranged_ability.split(" ")[1]
                        if extra[0] != "d":
                            extra = int(extra)
                        else:
                            extra = random.randint(1,int(extra[1]))
                        hits += extra
                    if hit == 6 and self.ranged_ability.split(" ")[0] == "lethal_hits":
                        hits -=1
                        wounds += 1
        else:
            for i in range(0, self.amount):
                hits += random.randint(1, int(self.shots[1]))

        if self.ranged_str == 2*target.toughness:
            to_wound = 4
        if self.ranged_str > target.toughness:
            to_wound = 3
        if self.ranged_str < target.toughness:
            to_wound = 5
        if self.ranged_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.ranged_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1
                if self.ranged_ability.split(" ")[0] == "Devastating_wounds":
                    wounds -= 1
                    x += self.ranged_dmg

        for i in range(0, wounds):
            save = random.randint(1,6)
            to_save = target.save+self.ranged_ap
            if target.cover == 1 and self.ranged_ability != "ignore cover":
                if self.ranged_ap > 0:
                    to_save -= 1
                else:
                    if target.save > 3:
                        to_save -= 1
            if save < to_save and save < target.invul:
                x += self.ranged_dmg

        #Purifiers
        if self.name == "Purifier Squad":
            for i in range(0, self.PA_shots*5):
                hit=random.randint(1,6)
                if hit >= self.PA_BS:
                    hits += 1

            if self.ranged_str == 2*target.toughness:
                to_wound = 4
            if self.ranged_str > target.toughness:
                to_wound = 3
            if self.ranged_str < target.toughness:
                to_wound = 5
            if 2*self.ranged_str <= target.toughness:
                to_wound = 6
            if self.ranged_str>= 2*target.toughness or target.kw == "infantry":
                to_wound = 2

            for i in range(0, hits):
                wound = random.randint(1,6)
                if wound >= to_wound:
                    wounds += 1

            for i in range(0, wounds):
                save = random.randint(1,6)
                to_save = target.save+self.PA_ap
                if target.cover == 1 and self.PA_ability != "ignore cover":
                    if self.PA_ap > 0:
                        to_save -= 1
                    else:
                        if target.save > 3:
                            to_save -= 1
                if save < to_save and save < target.invul:
                    x += self.PA_dmg

        print("Shooting:")
        print(f"5 man {self.name} with {self.weapon} deals {x} damage to {target.name}")

        hits = 0
        wounds = 0

        #default weapon
        if type(self.default_BS) is int:
            for i in range(0, def_shots*(5-self.amount-self.apothecary)):
                hit=random.randint(1,6)
                if hit >= self.default_BS:
                    hits += 1
                    if hit == 6 and self.default_ranged_ability.split(" ")[0] == "sustained_hits":
                        extra = self.default_ranged_ability.split(" ")[1]
                        if extra[0] != "d":
                            extra = int(extra)
                        else:
                            extra = random.randint(1,int(extra[1]))
                        hits += extra
                    if hit == 6 and self.default_ranged_ability.split(" ")[0] == "lethal_hits":
                        hits -=1
                        wounds += 1
        else:
            for i in range(0, 5-self.amount-self.apothecary):
                hits += random.randint(1, int(self.default_shots[1]))

        if self.default_ranged_str == target.toughness:
            to_wound = 4
        if self.default_ranged_str > target.toughness:
            to_wound = 3
        if self.default_ranged_str < target.toughness:
            to_wound = 5
        if self.default_ranged_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.default_ranged_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1
                if self.default_ranged_ability.split(" ")[0] == "Devastating_wounds":
                    wounds -= 1
                    x += self.default_ranged_dmg

        for i in range(0, wounds):
            save = random.randint(1,6)
            to_save = target.save+self.default_ranged_ap
            if target.cover == 1 and self.default_ranged_ability != "ignore cover":
                if self.default_ranged_ap > 0:
                    to_save -= 1
                else:
                    if target.save > 3:
                        to_save -= 1
            if save < to_save and save < target.invul:
                x += self.default_ranged_dmg

        hits = 0
        wounds = 0

        #specials
        if type(self.BS) is int:
            for i in range(0, self.shots*(self.amount_10 - self.amount)):
                hit=random.randint(1,6)
                if hit >= self.BS:
                    hits += 1
                    if hit == 6 and self.ranged_ability.split(" ")[0] == "sustained_hits":
                        extra = self.ranged_ability.split(" ")[1]
                        if extra[0] != "d":
                            extra = int(extra)
                        else:
                            extra = random.randint(1,int(extra[1]))
                        hits += extra
                    if hit == 6 and self.ranged_ability.split(" ")[0] == "lethal_hits":
                        hits -=1
                        wounds += 1
        else:
            for i in range(0, self.amount):
                hits += random.randint(1, int(self.shots[1]))

        if self.ranged_str == 2*target.toughness:
            to_wound = 4
        if self.ranged_str > target.toughness:
            to_wound = 3
        if self.ranged_str < target.toughness:
            to_wound = 5
        if self.ranged_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.ranged_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1
                if self.ranged_ability.split(" ")[0] == "Devastating_wounds":
                    wounds -= 1
                    x += self.ranged_dmg

        for i in range(0, wounds):
            save = random.randint(1,6)
            to_save = target.save+self.ranged_ap
            if target.cover == 1 and self.ranged_ability != "ignore cover":
                if self.ranged_ap > 0:
                    to_save -= 1
                else:
                    if target.save > 3:
                        to_save -= 1
            if save < to_save and save < target.invul:
                x += self.ranged_dmg

        #Purifiers
        if self.name == "Purifier Squad":
            for i in range(0, self.PA_shots*5):
                hit=random.randint(1,6)
                if hit >= self.PA_BS:
                    hits += 1

            if self.ranged_str == 2*target.toughness:
                to_wound = 4
            if self.ranged_str > target.toughness:
                to_wound = 3
            if self.ranged_str < target.toughness:
                to_wound = 5
            if 2*self.ranged_str <= target.toughness:
                to_wound = 6
            if self.ranged_str>= 2*target.toughness or target.kw == "infantry":
                to_wound = 2

            for i in range(0, hits):
                wound = random.randint(1,6)
                if wound >= to_wound:
                    wounds += 1

            for i in range(0, wounds):
                save = random.randint(1,6)
                to_save = target.save+self.PA_ap
                if target.cover == 1 and self.PA_ability != "ignore cover":
                    if self.PA_ap > 0:
                        to_save -= 1
                    else:
                        if target.save > 3:
                            to_save -= 1
                if save < to_save and save < target.invul:
                    x += self.PA_dmg


        print(f"10 man {self.name} with {self.weapon} deals {x} damage to {target.name}\n")

    def melee(self, target):
        x = 0
        hits = 0
        wounds = 0
        attacks5 = 5 * self.attacks
        attacks10 = 10 * self.attacks

        if self.armor == "power":
            attacks5 -= self.amount
            attacks10 -= self.amount_10

            for i in range(0, self.amount):
                hit=random.randint(1,6)
                if hit >= self.default_WS:
                    hits += 1

            if self.default_melee_str == target.toughness:
                to_wound = 4
            if self.default_melee_str > target.toughness:
                to_wound = 3
            if self.default_melee_str < target.toughness:
                to_wound = 5
            if self.default_melee_str >= 2*target.toughness:
                to_wound = 2
            if 2*self.default_melee_str <= target.toughness:
                to_wound = 6

            for i in range(0, hits):
                wound = random.randint(1,6)
                if wound >= to_wound:
                    wounds += 1

            for i in range(0, wounds):
                save = random.randint(1,6)
                if save < target.save+self.default_melee_ap and save < target.invul:
                    x += self.default_melee_dmg

        for i in range(0, attacks5):
                hit=random.randint(1,6)
                if hit >= self.WS:
                    hits += 1

        if self.melee_str == target.toughness:
            to_wound = 4
        if self.melee_str > target.toughness:
            to_wound = 3
        if self.melee_str < target.toughness:
            to_wound = 5
        if self.melee_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.melee_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1

        for i in range(0, wounds):
            save = random.randint(1,6)
            if save < target.save+self.melee_ap and save < target.invul:
                x += self.melee_dmg

        print("Melee combat:")
        print(f"5 man {self.name} deals {x} damage to {target.name}")

        hits = 0
        wounds = 0

        if self.armor == "power":
            for i in range(0, self.amount_10-self.amount):
                hit=random.randint(1,6)
                if hit >= self.default_WS:
                    hits += 1

            if self.default_melee_str == target.toughness:
                to_wound = 4
            if self.default_melee_str > target.toughness:
                to_wound = 3
            if self.default_melee_str < target.toughness:
                to_wound = 5
            if self.default_melee_str >= 2*target.toughness:
                to_wound = 2
            if 2*self.default_melee_str <= target.toughness:
                to_wound = 6

            for i in range(0, hits):
                wound = random.randint(1,6)
                if wound >= to_wound:
                    wounds += 1

            for i in range(0, wounds):
                save = random.randint(1,6)
                if save < target.save+self.default_melee_ap and save < target.invul:
                    x += self.default_melee_dmg

        for i in range(0, attacks10-attacks5):
                hit=random.randint(1,6)
                if hit >= self.WS:
                    hits += 1

        if self.melee_str == target.toughness:
            to_wound = 4
        if self.melee_str > target.toughness:
            to_wound = 3
        if self.melee_str < target.toughness:
            to_wound = 5
        if self.melee_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.melee_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1

        for i in range(0, wounds):
            save = random.randint(1,6)
            if save < target.save+self.melee_ap and save < target.invul:
                x += self.melee_dmg

        print(f"10 man {self.name} deals {x} damage to {target.name}\n")


    def __repr__(self):
        x = f"{self.name} with {self.weapon}:\n"
        x += f"Attacks: {self.attacks}\n"
        x += f"WS: {self.WS}\n"
        x += f"Melee STR: {self.melee_str}\n"
        x += f"Melee AP: {self.melee_ap}\n"
        x += f"Melee DMG: {self.melee_dmg}\n"
        x += f"Melee ability: {self.melee_ability}\n"
        x += f"Toughness: {self.toughness}\n"
        x += f"BS: {self.BS}\n"
        x += f"stormbolters in 5 man: {5-self.amount-self.apothecary}\n"
        x += f"special weapons in 5 man: {self.amount}\n"
        x += f"stormbolters in 10 man: {10-self.amount_10-self.apothecary}\n"
        x += f"special weapons in 10 man: {self.amount_10}\n"
        x += f"ranged STR: {self.ranged_str}\n"
        x += f"ranged AP: {self.ranged_ap}\n"
        x += f"ranged DMG: {self.ranged_dmg}\n"
        x += f"ranged ability: {self.ranged_ability}\n"
        if self.name == "Purifier Squad":
            x += f"Psychic Attack STR: {self.PA_str}\n"
            x += f"Psychic Attack AP: {self.PA_ap}\n"
            x += f"Psychic Attack DMG: {self.PA_dmg}\n"
            x += f"Psychic Attack ability: {self.PA_ability}\n"
        if self.cover == 0:
            x += "in cover? = No"
        else:
            x += "in cover? = Yes"
        return x



class Infantry (Inf_Weapon):
    def __init__ (self, weapon:str,cover:bool=False):
        super().__init__(weapon, cover)
        self.kw = "infantry"
        self.attacks = 3
        self.WS = 3
        self.melee_str = 6
        self.melee_ap = 2
        self.melee_dmg = 2
        self.melee_ability = ""
        self.default_attacks = 3
        self.default_WS = 3
        self.default_melee_str = 4
        self.default_melee_ap = 0
        self.default_melee_dmg = 1
        self.default_melee_ability = ""

class PowerArmor(Infantry):
    def __init__ (self, weapon:str, cover:bool=False):
        super().__init__(weapon, cover)
        self.armor = "power"
        self.toughness = 4
        self.save = 2
        self.invul = 7

class TermoArmor (Infantry):
    def __init__ (self, weapon: str, cover:bool=False):
        super().__init__(weapon,cover)
        self.armor = "termo"
        self.toughness = 5
        self.save = 2
        self.invul = 4

class StrikeSquad(PowerArmor):
    def __init__(self, weapon:str, cover:bool=False):
        super().__init__(weapon, cover)
        self.name = "Strike Squad"
        if weapon != "stormbolter":
            self.amount = 1
            self.amount_10 = 2

class Purifiers(PowerArmor):
    def __init__(self, weapon:str, cover:bool=False):
        super().__init__(weapon,cover)
        self.name = "Purifier Squad"
        if weapon != "stormbolter":
            self.amount = 2
            self.amount_10 = 4
        self.PA_shots = 1
        self.PA_BS = 3
        self.PA_str = 4
        self.PA_ap = 2
        self.PA_dmg = 1
        self.PA_ability = "ignore cover"

class Interceptors(PowerArmor):
    def __init__(self, weapon:str, cover:bool=False):
        super().__init__(weapon,cover)
        self.name = "Interceptor Squad"
        if weapon != "stormbolter":
            self.amount = 1
            self.amount_10 = 2

class Purgators(PowerArmor):
    def __init__(self, weapon:str, cover:bool=False):
        super().__init__(weapon,cover)
        self.name = "Purgation Squad"
        if weapon != "stormbolter":
            self.amount = 4
            self.amount_10 = 4

class Terminator(TermoArmor):
    def __init__(self, weapon:str, cover:bool=False):
        super().__init__(weapon,cover)
        self.name = "Terminator Squad"
        if weapon != "stormbolter":
            self.amount = 2
            self.amount_10 = 3
        self.apothecary = 1

class Paladin(TermoArmor):
    def __init__(self, weapon:str, cover:bool=False):
        super().__init__(weapon,cover)
        self.name = "Paladin Squad"
        self.attacks = 4
        self.WS = 2
        if weapon != "stormbolter":
            self.amount = 3
            self.amount_10 = 5
        self.apothecary = 1
