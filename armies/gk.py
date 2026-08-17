class Inf_Weapon():
    def __init__(self, weapon: str):
        self.apothecary = 0
        self.amount = 0
        self.amount_10 = 0
        match (weapon):
            case "stormbolter":
                self.shots = 2
                self.BS = 3
                self.ranged_str = 4
                self.ranged_ap = 0
                self.ranged_dmg = 1
                self.ranged_ability = "rapid_fire 2"
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
                self.shots = "6"
                self.BS = "torrent"
                self.ranged_str = 6
                self.ranged_ap = 1
                self.ranged_dmg = 1
                self.ranged_ability = ""

    def __repr__(self):
        return (
            f"{self.name}:\n"
            f"Attacks: {self.attacks}\n"
            f"WS: {self.WS}\n"
            f"Melee STR: {self.melee_str}\n"
            f"Melee AP: {self.melee_ap}\n"
            f"Melee DMG: {self.melee_dmg}\n"
            f"Melee ability: {self.melee_ability}\n"
            f"Toughness: {self.toughness}\n"
            f"BS: {self.BS}\n"
            f"stormbolters in 5 man: {5-self.amount-self.apothecary}\n"
            f"special weapons in 5 man: {self.amount}\n"
            f"stormbolters in 10 man: {10-self.amount_10-self.apothecary}\n"
            f"special weapons in 10 man: {self.amount_10}\n"
            f"ranged STR: {self.ranged_str}\n"
            f"ranged AP: {self.ranged_ap}\n"
            f"ranged DMG: {self.ranged_dmg}\n"
            f"ranged ability: {self.ranged_ability}"
            )


class Infantry (Inf_Weapon):
    def __init__ (self, weapon:str):
        super().__init__(weapon)
        self.attacks = 3
        self.WS = 3
        self.melee_str = 6
        self.melee_ap = 2
        self.melee_dmg = 2
        self.melee_ability = ""

class PowerArmor(Infantry):
    def __init__ (self, weapon:str):
        super().__init__(weapon)
        self.toughness = 4
        self.save = 3

class TermoArmor (Infantry):
    def __init__ (self, weapon: str):
        super().__init__(weapon)
        self.toughness = 5
        self.save = 2

class StrikeSquad(PowerArmor):
    def __init__(self, weapon:str):
        super().__init__(weapon)
        self.name = "Strike Squad"
        if weapon != "stormbolter":
            self.amount = 1
            self.amount_10 = 2


class Purifiers(PowerArmor):
    def __init__(self, weapon:str):
        super().__init__(weapon)
        self.name = "Purifier Squad"
        if weapon != "stormbolter":
            self.amount = 2
            self.amount_10 = 4
        self.PA_shots = 1
        self.PA_BS = 3
        self.PA_str = 4
        self.PA_ap = 2
        self.PA_dmg = 1
        self.PA_ability = "anti_infantry 2"


class Interceptors(PowerArmor):
    def __init__(self, weapon:str):
        super().__init__(weapon)
        self.name = "Interceptor Squad"
        if weapon != "stormbolter":
            self.amount = 1
            self.amount_10 = 2

class Purgators(PowerArmor):
    def __init__(self, weapon:str):
        super().__init__(weapon)
        self.name = "Purgation Squad"
        if weapon != "stormbolter":
            self.amount = 4
            self.amount_10 = 4

class Terminator(TermoArmor):
    def __init__(self, weapon:str):
        super().__init__(weapon)
        self.name = "Terminator Squad"
        if weapon != "stormbolter":
            self.amount = 2
            self.amount_10 = 3
        self.apothecary = 1

class Paladin(TermoArmor):
    def __init__(self, weapon:str):
        super().__init__(weapon)
        self.name = "Paladin Squad"
        self.attacks = 4
        self.WS = 2
        if weapon != "stormbolter":
            self.amount = 3
            self.amount_10 = 5
        self.apothecary = 1
