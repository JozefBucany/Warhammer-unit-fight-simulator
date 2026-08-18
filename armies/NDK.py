import random


class NDK():
    def __init__(self, meleewep:str|None=None, weapon1: str|None=None, weapon2:str|None=None, cover: bool = False):
        self.name = "Nemesis Dreadknight"
        self.cover = 0
        if cover:
            self.cover = 1
        self.toughness = 8
        self.save = 2
        self.invul = 4
        self.meleewep = meleewep
        if self.meleewep is None:
            self.meleewep = "fists"
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        match (meleewep):
            case "hammer":
                self.melee_attacks = 5
                self.WS = 3
                self.melee_str = 14
                self.melee_ap = 3
                self.melee_dmg = "d6+1"
            case "sword":
                self.strike_attacks = 5
                self.WS = 2
                self.strike_str = 10
                self.strike_ap = 2
                self.strike_dmg = "d6"
                self.sweep_attacks = 10
                self.WS = 2
                self.sweep_str = 5
                self.sweep_ap = 1
                self.sweep_dmg = 1
            case _:
                self.melee_attacks = 6
                self.WS = 2
                self.melee_str = 6
                self.melee_ap = 1
                self.melee_dmg = 1

        match (weapon1):
            case "psycannon":
                self.w1_shots = 6
                self.w1_BS = 3
                self.w1_ranged_str = 10
                self.w1_ranged_ap = 2
                self.w1_ranged_dmg = 3
                self.w1_ranged_ability = "ignore cover"
            case "psilencer":
                self.w1_shots = 12
                self.w1_BS = 3
                self.w1_ranged_str = 6
                self.w1_ranged_ap = 0
                self.w1_ranged_dmg = 1
                self.w1_ranged_ability = "sustained_hits 1"
            case "incinerator":
                self.w1_shots = "2d6"
                self.w1_BS = "torrent"
                self.w1_ranged_str = 6
                self.w1_ranged_ap = 1
                self.w1_ranged_dmg = 1
                self.w1_ranged_ability = "ignore cover"
            case _:
                pass
        match (weapon2):
            case "psycannon":
                self.w2_shots = 6
                self.w2_BS = 3
                self.w2_ranged_str = 10
                self.w2_ranged_ap = 2
                self.w2_ranged_dmg = 3
                self.w2_ranged_ability = "ignore cover"
            case "psilencer":
                self.w2_shots = 12
                self.w2_BS = 3
                self.w2_ranged_str = 6
                self.w2_ranged_ap = 0
                self.w2_ranged_dmg = 1
                self.w2_ranged_ability = "sustained_hits 1"
            case "incinerator":
                self.w2_shots = "2d6"
                self.w2_BS = "torrent"
                self.w2_ranged_str = 6
                self.w2_ranged_ap = 1
                self.w2_ranged_dmg = 1
                self.w2_ranged_ability = "ignore cover"
            case _:
                pass

    def shoot(self, target):
        x = 0
        hits = 0
        wounds = 0

        #weapon 1
        if type(self.w1_BS) is int:
            for i in range(0, self.w1_shots):
                hit=random.randint(1,6)
                if hit >= self.w1_BS:
                    hits += 1
                    if hit == 6 and self.w1_ranged_ability.split(" ")[0] == "sustained_hits":
                        extra = self.w1_ranged_ability.split(" ")[1]
                        if extra[0] != "d":
                            extra = int(extra)
                        else:
                            extra = random.randint(1,int(extra[1]))
                        hits += extra
                    if hit == 6 and self.w1_ranged_ability.split(" ")[0] == "lethal_hits":
                        hits -=1
                        wounds += 1
        else:
            for i in range (0, int(self.w1_shots[0])):
                hits += random.randint(1, int(self.w1_shots[2]))

        if self.w1_ranged_str == target.toughness:
            to_wound = 4
        if self.w1_ranged_str > target.toughness:
            to_wound = 3
        if self.w1_ranged_str < target.toughness:
            to_wound = 5
        if self.w1_ranged_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.w1_ranged_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1
                if self.w1_ranged_ability.split(" ")[0] == "Devastating_wounds":
                    wounds -= 1
                    x += self.w1_ranged_dmg

        for i in range(0, wounds):
            save = random.randint(1,6)
            to_save = target.save+self.w1_ranged_ap
            if target.cover == 1 and self.w1_ranged_ability != "ignore cover":
                if self.w1_ranged_ap > 0:
                    to_save -= 1
                else:
                    if target.save > 3:
                        to_save -= 1
            if save < to_save and save < target.invul:
                x += self.w1_ranged_dmg

        hits = 0
        wounds = 0

        #weapon 2
        if type(self.w2_BS) is int:
            for i in range(0, self.w2_shots):
                hit=random.randint(1,6)
                if hit >= self.w2_BS:
                    hits += 1
                    if hit == 6 and self.w2_ranged_ability.split(" ")[0] == "sustained_hits":
                        extra = self.w2_ranged_ability.split(" ")[1]
                        if extra[0] != "d":
                            extra = int(extra)
                        else:
                            extra = random.randint(1,int(extra[1]))
                        hits += extra
                    if hit == 6 and self.w2_ranged_ability.split(" ")[0] == "lethal_hits":
                        hits -=1
                        wounds += 1
        else:
            for i in range (0, int(self.w2_shots[0])):
                hits += random.randint(1, int(self.w2_shots[2]))

        if self.w2_ranged_str == target.toughness:
            to_wound = 4
        if self.w2_ranged_str > target.toughness:
            to_wound = 3
        if self.w2_ranged_str < target.toughness:
            to_wound = 5
        if self.w2_ranged_str >= 2*target.toughness:
            to_wound = 2
        if 2*self.w2_ranged_str <= target.toughness:
            to_wound = 6

        for i in range(0, hits):
            wound = random.randint(1,6)
            if wound >= to_wound:
                wounds += 1
                if self.w2_ranged_ability.split(" ")[0] == "Devastating_wounds":
                    wounds -= 1
                    x += self.w2_ranged_dmg

        for i in range(0, wounds):
            save = random.randint(1,6)
            to_save = target.save+self.w2_ranged_ap
            if target.cover == 1 and self.w2_ranged_ability != "ignore cover":
                if self.w2_ranged_ap > 0:
                    to_save -= 1
                else:
                    if target.save > 3:
                        to_save -= 1
            if save < to_save and save < target.invul:
                x += self.w2_ranged_dmg

        print("\nShooting:")
        print(f"{self.name} with {self.weapon1} and {self.weapon2} deals {x} damage to {target.name}")

    def melee(self, target):
        x = 0
        hits = 0
        wounds = 0

        #hammer
        if self.meleewep == "hammer" or self.meleewep == "fists":
            for i in range(0, self.melee_attacks):
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
                    if self.meleewep == "hammer":
                        x += 1+random.randint(1,6)
                    else:
                        x += self.melee_dmg

            print("\nMelee combat:")
            print(f"{self.name} with {self.meleewep} deals {x} damage to {target.name}")

        #sword
        if self.meleewep == "sword":
            for i in range(0, self.strike_attacks):
                    hit=random.randint(1,6)
                    if hit >= self.WS:
                        hits += 1

            if self.strike_str == target.toughness:
                to_wound = 4
            if self.strike_str > target.toughness:
                to_wound = 3
            if self.strike_str < target.toughness:
                to_wound = 5
            if self.strike_str >= 2*target.toughness:
                to_wound = 2
            if 2*self.strike_str <= target.toughness:
                to_wound = 6

            for i in range(0, hits):
                wound = random.randint(1,6)
                if wound >= to_wound:
                    wounds += 1

            for i in range(0, wounds):
                save = random.randint(1,6)
                if save < target.save+self.strike_ap and save < target.invul:
                    x += random.randint(1,6)

            print("\nMelee combat:")
            print(f"{self.name} with {self.meleewep} using Strike deals {x} damage to {target.name}")

            x=0
            hits = 0
            wounds = 0

            for i in range(0, self.sweep_attacks):
                    hit=random.randint(1,6)
                    if hit >= self.WS:
                        hits += 1

            if self.sweep_str == target.toughness:
                to_wound = 4
            if self.sweep_str > target.toughness:
                to_wound = 3
            if self.sweep_str < target.toughness:
                to_wound = 5
            if self.sweep_str >= 2*target.toughness:
                to_wound = 2
            if 2*self.sweep_str <= target.toughness:
                to_wound = 6

            for i in range(0, hits):
                wound = random.randint(1,6)
                if wound >= to_wound:
                    wounds += 1

            for i in range(0, wounds):
                save = random.randint(1,6)
                if save < target.save+self.sweep_ap and save < target.invul:
                    x += self.sweep_dmg

            print(f"{self.name} with {self.meleewep} using sweep deals {x} damage to {target.name}")

    def __repr__(self):
        x = f"{self.name} with {self.meleewep}"
        if self.weapon1 is not None:
            x+=f", {self.weapon1}"
        if self.weapon2 is not None:
            x+=f" {self.weapon2}"
        x+=":\n"
        if self.meleewep == "hammer":
            x += f"Attacks: {self.melee_attacks}\n"
            x += f"WS: {self.WS}\n"
            x += f"Melee STR: {self.melee_str}\n"
            x += f"Melee AP: {self.melee_ap}\n"
            x += f"Melee DMG: {self.melee_dmg}\n"
        if self.meleewep == "sword":
            x += f"Strike attacks: {self.strike_attacks}\n"
            x += f"Strike WS: {self.WS}\n"
            x += f"Strike STR: {self.strike_str}\n"
            x += f"Strike AP: {self.strike_ap}\n"
            x += f"Strike DMG: {self.strike_dmg}\n"
            x += f"Sweep attacks: {self.sweep_attacks}\n"
            x += f"Sweep WS: {self.WS}\n"
            x += f"Sweep STR: {self.sweep_str}\n"
            x += f"Sweep AP: {self.sweep_ap}\n"
            x += f"Sweep DMG: {self.sweep_dmg}\n"
        if self.meleewep == "fists":
            x += f"Attacks: {self.melee_attacks}\n"
            x += f"WS: {self.WS}\n"
            x += f"Melee STR: {self.melee_str}\n"
            x += f"Melee AP: {self.melee_ap}\n"
            x += f"Melee DMG: {self.melee_dmg}\n"
        x += f"Toughness: {self.toughness}\n"
        if self.weapon1 is not None:
            x += f"{self.weapon1} shots: {self.w1_shots}\n"
            x += f"{self.weapon1} BS: {self.w1_BS}\n"
            x += f"{self.weapon1} ranged STR: {self.w1_ranged_str}\n"
            x += f"{self.weapon1} ranged AP: {self.w1_ranged_ap}\n"
            x += f"{self.weapon1} ranged DMG: {self.w1_ranged_dmg}\n"
            x += f"{self.weapon1} ranged ability: {self.w1_ranged_ability}\n"
        if self.weapon2 is not None:
            x += f"{self.weapon2} shots: {self.w2_shots}\n"
            x += f"{self.weapon2} BS: {self.w2_BS}\n"
            x += f"{self.weapon2} ranged STR: {self.w2_ranged_str}\n"
            x += f"{self.weapon2} ranged AP: {self.w2_ranged_ap}\n"
            x += f"{self.weapon2} ranged DMG: {self.w2_ranged_dmg}\n"
            x += f"{self.weapon2} ranged ability: {self.w2_ranged_ability}\n"
        if self.cover == 0:
            x += "in cover? = No"
        else:
            x += "in cover? = Yes"
        return x
