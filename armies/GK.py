class Weapon():
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        if weapons_list5 is None:
            weapons_list5 = []
        if weapons_list10 is None:
            weapons_list10 = []
        self.crit_h_on = 6
        self.crit_w_on = 6
        self.cover = 0
        if cover:
            self.cover = 1
        self.stealth = 0
        if stealth:
            self.stealth = 1
        self.minushit = False
        self.models = 5
        self.fortyk = True
        self.aos = False
        self.fnp = 7
        self.fnpm = 7
        self.fnpp = 7
        self.amount5_psy = 0
        self.amount5_psi = 0
        self.amount5_inci = 0
        self.amount10_psy = 0
        self.amount10_psi = 0
        self.amount10_inci = 0
        self.melee_weapons5 = [[0,3,3,4,0,1,{}]]
        self.melee_weapons5.append([5,3,3,6,2,2,{"psychic":True}])
        self.melee_weapons10 = [[0,3,3,4,0,1,{}]]
        self.melee_weapons10.append([5,3,3,6,2,2,{"psychic":True}])
        self.ranged_weapons5 = [[5,2,3,4,0,1,{"rapid_fire": 2}]]
        self.ranged_weapons10 = [[5,2,3,4,0,1,{"rapid_fire": 2}]]
        for weapon in weapons_list5:
            match (weapon):
                case "psycannon":
                    self.melee_weapons5[0][0] += 1
                    self.melee_weapons5[1][0] -= 1
                    self.ranged_weapons5[0][0] -= 1
                    if self.amount5_psy == 0:
                        self.ranged_weapons5.append([1,3,3,8,1,2,{"psychic":True}])
                        self.amount5_psy += 1
                    else:
                        for asdf in self.ranged_weapons5:
                            if asdf[6] == {"psychic":True}:
                                asdf[0] += 1
                case "psilencer":
                    self.melee_weapons5[0][0] += 1
                    self.melee_weapons5[1][0] -= 1
                    self.ranged_weapons5[0][0] -= 1
                    if self.amount5_psi == 0:
                        self.ranged_weapons5.append([1,6,3,5,0,1,{"psychic":True, "sustained_hits": 1}])
                        self.amount5_psi += 1
                    else:
                        for asdf in self.ranged_weapons5:
                            if "sustained_hits" in asdf[6]:
                                asdf[0] += 1
                case "incinerator":
                    self.melee_weapons5[0][0] += 1
                    self.melee_weapons5[1][0] -= 1
                    self.ranged_weapons5[0][0] -= 1
                    if self.amount5_inci == 0:
                        self.ranged_weapons5.append([1,"d6","torrent",6,1,1,{"ignore_cover":True}])
                        self.amount5_inci += 1
                    else:
                        for asdf in self.ranged_weapons5:
                            if "ignore_cover" in asdf[6]:
                                asdf[0] += 1
                case _:
                    pass

        for weapon in weapons_list10:
            match (weapon):
                case "psycannon":
                    self.melee_weapons10[0][0] += 1
                    self.melee_weapons10[1][0] -= 1
                    self.ranged_weapons10[0][0] -= 1
                    if self.amount10_psy == 0:
                        self.ranged_weapons10.append([1,3,3,8,1,2,{"psychic":True}])
                        self.amount10_psy += 1
                    else:
                        for asdf in self.ranged_weapons10:
                            if asdf[6] == {"psychic":True}:
                                asdf[0] += 1
                case "psilencer":
                    self.melee_weapons10[0][0] += 1
                    self.melee_weapons10[1][0] -= 1
                    self.ranged_weapons10[0][0] -= 1
                    if self.amount10_psi == 0:
                        self.ranged_weapons10.append([1,6,3,5,0,1,{"psychic":True, "sustained_hits": 1}])
                        self.amount10_psi += 1
                    else:
                        for asdf in self.ranged_weapons10:
                            if "sustained_hits" in asdf[6]:
                                asdf[0] += 1
                case "incinerator":
                    self.melee_weapons10[0][0] += 1
                    self.melee_weapons10[1][0] -= 1
                    self.ranged_weapons10[0][0] -= 1
                    if self.amount10_inci == 0:
                        self.ranged_weapons10.append([1,"d6","torrent",6,1,1,{"ignore_cover":True}])
                        self.amount10_inci += 1
                    else:
                        for asdf in self.ranged_weapons10:
                            if "ignore_cover" in asdf[6]:
                                asdf[0] += 1
                case _:
                    pass

    def __repr__(self):
        x = "================================================================\n"
        x += f"{self.name}:\n"
        x += "================================================================\n"
        x += f"Toughness: {self.toughness}\n"
        x += f"armor save: {self.save}\n"
        if self.invul < 7:
            x+= f"Invulnerable save: {self.invul}\n"
        if self.fnp <7:
            x+= f"Feel no pain: {self.fnp}"
        if self.cover == 0:
            x += "in cover? = No\n"
        else:
            x += "in cover? = Yes\n"
        if self.name == "Purifier Squad" and self.ranged_weapons5[2][1] == 2:
            x += "led by Castelan Crowe\n"
        if self.minushit is True:
            x += "led by Grandmaster Voldus\n"
        if "lethal_hits" in self.melee_weapons5[0][6]:
            x += "led by Brother Captain\n"
        if self.fnpp == 4:
            x += "led by Brotherhood Librarian\n"
        return x



class Infantry (Weapon):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.kw = ["infantry","psyker"]

class PowerArmor(Infantry):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.hp = 2
        self.toughness = 4
        self.save = 2
        self.invul = 7

class TermoArmor (Infantry):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, voldus = False, captain=False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.melee_weapons5[0][0] = 0
        self.melee_weapons5[1][0] = self.models
        if captain:
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,4,2,6,2,2,{"psychic":True}])
            for item in self.melee_weapons5:
                if "lethal_hits" not in item[6]:
                    item[6]["lethal_hits"]= True
        if voldus:
            self.minushit = True
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,5,2,10,2,3,{"psychic":True}])
        if libi and self.fnpp > 4:
            self.fnpp = 4
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,4,2,10,2,3,{"psychic":True}])
        self.kw.append("terminator")
        self.hp = 3
        self.toughness = 5
        self.save = 2
        self.invul = 4

class StrikeSquad(PowerArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover,stealth)
        self.name = "Strike Squad"

class Purifiers(PowerArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, crowe = False):
        super().__init__(weapons_list5, weapons_list10, cover,stealth)
        self.name = "Purifier Squad"
        self.ranged_weapons5.append([5,1,3,4,2,1,{"anti-infantry": 2, "ignore_cover":True}])
        self.ranged_weapons10.append([5,1,3,4,2,1,{"anti-infantry": 2, "ignore_cover":True}])
        if crowe:
            self.kw.append("character")
            self.ranged_weapons5[2][1] = 2
            self.ranged_weapons5.append([1,2,2,4,0,1,{"rapid_fire":2}])
            self.ranged_weapons5.append([1,3,2,4,2,1,{"anti-infantry": 2, "ignore_cover":True}])
            self.melee_weapons5.append([1,5,2,6,2,2,{"devastating_wounds":True}])
        for item in self.melee_weapons5:
            item[6]["twin-linked"]=True
        for item in self.ranged_weapons5:
            item[6]["twin-linked"]=True
        for item in self.melee_weapons10:
            item[6]["twin-linked"]=True
        for item in self.ranged_weapons10:
            item[6]["twin-linked"]=True

class Interceptors(PowerArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover,stealth)
        self.name = "Interceptor Squad"

class Purgators(PowerArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Purgation Squad"

class Terminator(TermoArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, apothecary = False, voldus = False, captain = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Terminator Squad"
        self.melee_weapons5[0][0] = 0
        self.melee_weapons5[1][0] = 5
        self.melee_weapons10[0][0] = 0
        self.melee_weapons10[1][0] = 5
        if apothecary:
            self.ranged_weapons5[0][0] -= 1
        for item in self.melee_weapons5:
            item[6]["GKtermobuff"] = True
        for item in self.melee_weapons10:
            item[6]["GKtermobuff"] = True

class Paladin(TermoArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, ancient_weapon: list[str] = ["stormbolter"], cover: bool = False, stealth = False, apothecary = False, voldus = False, captain = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Paladin Squad"
        self.melee_weapons5[1][1] = 4
        self.melee_weapons5[1][6]["charge(+1 dmg)"] = True
        self.melee_weapons10[1][6]["charge(+1 dmg)"] = True
        self.melee_weapons5[1][2] = 2
        self.melee_weapons10[1][1] = 4
        self.melee_weapons10[1][2] = 2
        self.melee_weapons5[0][0] = 0
        self.melee_weapons5[1][0] = 5
        self.melee_weapons10[0][0] = 0
        self.melee_weapons10[1][0] = 5
        if apothecary:
            self.ranged_weapons5[0][0] -= 1
        match (ancient_weapon):
                case "psycannon":
                    self.ranged_weapons10[0][0] -= 1
                    if self.amount10_psy == 0:
                        self.ranged_weapons10.append([1,3,3,8,1,2,{"psychic":True}])
                        self.amount10_psy += 1
                    else:
                        for asdf in self.ranged_weapons10:
                            if asdf[6] == {"psychic":True}:
                                asdf[0] += 1
                case "psilencer":
                    self.ranged_weapons10[0][0] -= 1
                    if self.amount10_psi == 0:
                        self.ranged_weapons10.append([1,6,3,5,0,1,{"psychic":True, "sustained_hits": 1}])
                        self.amount10_psi += 1
                    else:
                        for asdf in self.ranged_weapons10:
                            if "sustained_hits" in asdf[6]:
                                asdf[0] += 1
                case "incinerator":
                    self.ranged_weapons10[0][0] -= 1
                    if self.amount10_inci == 0:
                        self.ranged_weapons10.append([1,"d6","torrent",6,1,1,{"ignore_cover":True}])
                        self.amount10_inci += 1
                    else:
                        for asdf in self.ranged_weapons10:
                            if "ignore_cover" in asdf[6]:
                                asdf[0] += 1
                case _:
                    pass


class Brotherhood_Champion(PowerArmor):
    def __init__(self, weapons_list5: list[str] = ["stormbolter"], weapons_list10: list[str] = ["stormbolter"], cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Brotherhood Champion"
        self.kw.append("character")
        self.models = 1
        self.hp = 4
        self.invul = 4
        self.melee_weapons5[1][0] = 1
        self.melee_weapons5[1][1] = 5
        self.ranged_weapons5[0][0] = 1

class Castellan_Crowe(PowerArmor):
    def __init__(self, weapons_list5: list[str] = ["stormbolter"], weapons_list10: list[str] = ["stormbolter"], cover: bool = False, stealth = False, crowe = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Castelan Crowe"
        self.kw.append("character")
        self.models = 1
        self.hp = 5
        self.invul = 4
        self.ranged_weapons5[0][0] = 1
        self.ranged_weapons5[0][2] = 2
        self.ranged_weapons5.append([1,3,2,4,2,1,{"anti-infantry": 2, "ignore_cover":True}])
        if crowe:
            self.ranged_weapons5[1][1] = 4
        self.melee_weapons5[1][0] = 1
        self.melee_weapons5[1][1] = 5
        self.melee_weapons5[1][2] = 2
        self.melee_weapons5[1][6] = {"devastating_wounds":True}

class Techmarine(PowerArmor):
    def __init__(self, weapons_list5: list[str] = ["stormbolter"], weapons_list10: list[str] = ["stormbolter"], cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Brotherhood Techmarine"
        self.kw.append("character")
        self.models = 1
        self.hp = 4
        self.melee_weapons5 = [[1,4,3,6,2,2,{}]]
        self.melee_weapons5.append([1,1,3,8,2,3,{}])
        self.ranged_weapons5 = [[1,3,2,5,1,2,{}]]
        self.ranged_weapons5.append([1,1,2,4,1,2,{"anti-vehicle":2}])

class TermoChar(TermoArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, voldus = False, captain = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, voldus, captain,libi)
        self.name = "Terminator Character"
        self.kw.append("character")
        self.models = 1
        self.hp = 5
        self.melee_weapons5[0][0] = 0
        self.melee_weapons5[1][0] = 1
        self.melee_weapons5[1][1] = 4
        self.melee_weapons5[1][2] = 2
        if weapons_list5 is None:
            self.ranged_weapons5[0][0] = 1
        else:
            self.ranged_weapons5[0][0] = 0
        for item in self.ranged_weapons5:
            if type(item[2]) is int:
                item[2] = 2

class Brother_Captain(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, captain = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, captain=captain)
        self.name = "Brother Captain"

class Librarian(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, libi=libi)
        self.name = "Brotherhood Librarian"
        self.melee_weapons5[1][4] = 1
        if "combi-weapon" in weapons_list5:
            self.ranged_weapons5 = [[1,1,4,4,0,1,{"rapid_fire":1,"anti-infantry":4, "devastating_wounds":True}]]
        self.ranged_weapons5.append([1,"d6+3",3,8,2,2,{"blast": True, "psychic":True}])

class Grandmaster(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Grandmaster"
        self.melee_weapons5[1][1] = 5
        for item in self.ranged_weapons5:
            if type(item[2]) is int:
                item[2] = 2

class GM_Voldus(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, voldus = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, voldus=voldus)
        self.name = "Grandmaster Voldus"
        self.melee_weapons5[1][1] = 5
        self.melee_weapons5[1][3] = 10
        self.melee_weapons5[1][5] = 3
        self.ranged_weapons5[0][2] = 2

class Chaplain(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Brotherhood Chaplain"
        self.melee_weapons5[1][1] = 5
        self.melee_weapons5[1][4] = 1

class TestUnit(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, voldus = False, captain = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, voldus, captain, libi)
        self.name = "Test Unit with a LOT of weapons"
        self.ranged_weapons5 = []
        self.melee_weapons5 = []
        self.ranged_weapons5.append([1,5,2,8,3,3,{"psychic":True, "rapid_fire":1}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"rapid_fire":"d3"}])
        self.ranged_weapons5.append([1,5,2,3,3,3,{"anti-infantry":2}])
        self.ranged_weapons5.append([1,5,2,3,3,3,{"anti-vehicle":2}])
        self.ranged_weapons5.append([1,5,2,3,3,3,{"anti-psyker":2}])
        self.ranged_weapons5.append([1,5,2,3,3,3,{"anti-monster":2}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"blast":True}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"conversion":True}])
        self.ranged_weapons5.append([1,5,4,8,3,3,{"heavy":True}])
        self.ranged_weapons5.append([1,5,4,8,3,3,{"conversion":True,"heavy":True}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"devastating_wounds":True}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"hazardous":True}])
        self.ranged_weapons5.append([1,5,2,8,2,3,{"ignore_cover":True}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"lethal_hits":True}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"melta":3}])
        self.ranged_weapons5.append([1,5,2,8,3,3,{"sustained_hits":"d3"}])
        self.ranged_weapons5.append([1,5,2,4,3,3,{"twin-linked":True}])
        self.ranged_weapons5.append([1,5,"torrent",8,3,3,{}])
        self.ranged_weapons5.append([1,"2d6",2,8,3,3,{}])
        self.ranged_weapons5.append([1,"2d6+2",2,8,3,3,{}])
        self.ranged_weapons5.append([1,"2d6+2","torrent",8,3,3,{}])
        self.melee_weapons5.append([1,5,2,3,3,3,{"anti-infantry":2}])
        self.melee_weapons5.append([1,5,2,3,3,3,{"anti-vehicle":2}])
        self.melee_weapons5.append([1,5,2,3,3,3,{"anti-psyker":2}])
        self.melee_weapons5.append([1,5,2,3,3,3,{"anti-monster":2}])
        self.melee_weapons5.append([1,5,2,8,3,3,{"devastating_wounds":True}])
        self.melee_weapons5.append([1,5,2,8,3,3,{"hazardous":True}])
        self.melee_weapons5.append([1,5,2,4,3,3,{"lance":True}])
        self.melee_weapons5.append([1,5,2,8,3,3,{"lethal_hits":True}])
        self.melee_weapons5.append([1,5,2,8,3,3,{"sustained_hits":1}])
        self.melee_weapons5.append([1,5,2,4,3,3,{"twin-linked":True}])
        self.melee_weapons5.append([1,"d6",2,8,3,3,{"psychic":True, }])
        self.melee_weapons5.append([1,"d6+3",2,8,3,3,{"psychic":True, }])
