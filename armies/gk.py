class Base():
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, champ = False, tech = False, crowe= False, voldus = False, captain=False, libi = False):
        if weapons_list5 is None:
            weapons_list5 = []
        if weapons_list10 is None:
            weapons_list10 = []
        self.champ = champ
        self.tech = tech
        self.crowe = crowe
        self.voldus = voldus
        self.captain = captain
        self.libi = libi
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
        if self.crowe:
            x += "led by Castelan Crowe\n"
        if self.tech:
            x += "led by Techmarine\n"
        if self.champ:
            x += "led by Brotherhood champion\n"
        if self.voldus:
            x += "led by Grandmaster Voldus\n"
        if self.captain:
            x += "led by Brother Captain\n"
        if self.libi:
            x += "led by Brotherhood Librarian\n"
        return x



class Infantry (Base):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, champ = False, tech = False, crowe= False, voldus = False, captain=False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth,champ = champ, tech = tech, crowe=crowe,voldus = voldus, captain = captain, libi = libi)
        self.kw = ["infantry","psyker"]

class PowerArmor(Infantry):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, champ = False, tech = False, crowe= False, voldus = False, captain=False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth,champ = champ, tech = tech, crowe = crowe,voldus = voldus, captain = captain, libi = libi)
        self.hp = 2
        self.toughness = 4
        self.save = 2
        self.invul = 7

class TermoArmor (Infantry):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, voldus = False, captain=False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth,voldus = voldus, captain = captain, libi = libi)
        self.melee_weapons5[0][0] = 0
        self.melee_weapons5[1][0] = 5
        self.kw.append("terminator")
        self.hp = 3
        self.toughness = 5
        self.save = 2
        self.invul = 4

class StrikeSquad(PowerArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, champ = False, tech = False):
        super().__init__(weapons_list5, weapons_list10, cover,stealth,champ = champ)
        self.name = "Strike Squad"
        if champ:
            self.melee_weapons5.append([1,5,2,6,2,2,{"psychic":True}])
            self.ranged_weapons5.append([1,2,2,4,0,1,{"rapid_fire":2}])
        if tech:
            self.melee_weapons5.append([1,4,3,6,2,2,{}])
            self.melee_weapons5.append([1,1,3,8,2,3,{}])
            self.melee_weapons5.append([1,3,2,5,1,2,{}])
            self.ranged_weapons5.append([1,1,2,4,1,2,{"anti-vehicle":2}])

class Purifiers(PowerArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, crowe= False):
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
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, champ = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth,champ = champ)
        self.name = "Purgation Squad"
        if champ:
            self.melee_weapons5.append([1,5,2,6,2,2,{"psychic":True}])
            self.ranged_weapons5.append([1,2,2,4,0,1,{"rapid_fire":2}])

class Terminator(TermoArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, apothecary = False, voldus = False, captain = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, voldus=voldus, captain=captain, libi=libi)
        self.name = "Terminator Squad"
        self.melee_weapons5[0][0] = 0
        self.melee_weapons5[1][0] = 5
        self.melee_weapons10[0][0] = 0
        self.melee_weapons10[1][0] = 5
        if apothecary:
            self.ranged_weapons5[0][0] -= 1
        if captain:
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,4,2,6,2,2,{"psychic":True}])
            for item in self.melee_weapons5:
                item[6]["lethal_hits"]= True
        if voldus:
            self.minushit = True
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,5,2,10,2,3,{"psychic":True}])
        if libi:
            if self.fnpp > 4:
                self.fnpp = 4
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,4,2,6,1,2,{"psychic":True}])
        for item in self.melee_weapons5:
            item[6]["GKtermobuff"] = True
        for item in self.melee_weapons10:
            item[6]["GKtermobuff"] = True

class Paladin(TermoArmor):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, ancient_weapon: list[str] = ["stormbolter"], cover: bool = False, stealth = False, apothecary = False, voldus = False, captain = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, voldus=voldus, captain=captain, libi=libi)
        self.name = "Paladin Squad"
        self.melee_weapons5[1][1] = 4
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
        if captain:
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,4,2,6,2,2,{"psychic":True}])
            for item in self.melee_weapons5:
                item[6]["lethal_hits"]= True
        if voldus:
            self.minushit = True
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,5,2,10,2,3,{"psychic":True}])
        if libi:
            if self.fnpp > 4:
                self.fnpp = 4
            self.ranged_weapons5[0][0] += 1
            self.melee_weapons5.append([1,4,2,6,1,2,{"psychic":True}])
        for item in self.melee_weapons5:
            item[6]["charge(+1 dmg)"] = True
        for item in self.melee_weapons10:
            item[6]["charge(+1 dmg)"] = True


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
        super().__init__(weapons_list5, weapons_list10, cover, stealth,crowe = crowe)
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
        super().__init__(weapons_list5, weapons_list10, cover, stealth, voldus=voldus, captain=captain,libi=libi)
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
        if captain:
            for item in self.melee_weapons5:
                item[6]["lethal_hits"]= True

class Librarian(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False, libi = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth, libi=libi)
        self.name = "Brotherhood Librarian"
        self.melee_weapons5[1][4] = 1
        if "combi-weapon" in weapons_list5:
            self.ranged_weapons5 = [[1,1,4,4,0,1,{"rapid_fire":1,"anti-infantry":4, "devastating_wounds":True}]]
        self.ranged_weapons5.append([1,"d6+3",3,8,2,2,{"blast": True, "psychic":True}])
        if libi:
            if self.fnpp > 4:
                self.fnpp = 4

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
        if voldus:
            self.minushit = True

class Chaplain(TermoChar):
    def __init__(self, weapons_list5: list[str]|None = None, weapons_list10: list[str]|None = None, cover: bool = False, stealth = False):
        super().__init__(weapons_list5, weapons_list10, cover, stealth)
        self.name = "Brotherhood Chaplain"
        self.melee_weapons5[1][1] = 5
        self.melee_weapons5[1][4] = 1

class NDK(Base):
    def __init__(self, meleewep:str|None=None, weapons:list[str|None]=[], cover: bool = False, stealth = False,tech=False):
        super().__init__(cover = cover,stealth =stealth,tech = tech)
        self.name = "Nemesis Dreadknight"
        self.models = 1
        self.kw = ["psyker", "vehicle","walker"]
        self.hp = 13
        self.toughness = 8
        self.save = 2
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,6,1,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        match (meleewep):
            case "hammer":
                self.melee_weapons5=[[1,5,3,14,3,"d6+1",{"psychic": True}]]
            case "flail":
                self.melee_weapons5=[[1,10,2,5,1,2,{"psychic": True}]]
            case "mace":
                self.melee_weapons5=[[1,5,2,6,3,3,{"anti-character": 2, "psychic": True}]]
            case "sword":
                self.melee_weapons5=[[1,5,2,10,2,"d6",{"strike":True, "psychic": True}], [0,10,2,5,1,1,{"sweep":True, "psychic": True}]]
            case _:
                pass
        for item in weapons:
            match (item):
                case "psycannon":
                    self.ranged_weapons5.append([1,6,3,10,2,3,{"ignore_cover":True, "psychic": True}])
                case "psilencer":
                    self.ranged_weapons5.append([1,12,3,6,0,1,{"sustained_hits":1, "psychic": True}])
                case "incinerator":
                    self.ranged_weapons5.append([1,"2d6","torrent",6,1,1,{"ignore_cover":True}])
                case "sublimator":
                    self.ranged_weapons5.append([1,2,3,9,4,"d6",{"melta":4,"twin-linked":True, "psychic": True}])
                case "fragstorm":
                    self.ranged_weapons5.append([1,"d6",3,4,0,1,{"blast":True}])
                case _:
                    pass
        if tech:
            for item in self.melee_weapons5:
                item[6]["+1_to_hit"]=True
            for item in self.ranged_weapons5:
                item[6]["+1_to_hit"]=True

class GMNDK(NDK):
    def __init__(self, meleewep:str|None=None, weapons:list[str|None]=[], cover: bool = False, stealth = False,tech = False):
        super().__init__(meleewep, weapons, cover,stealth,tech = tech)
        self.kw.append("character")
        self.name = "Grandmaster is Nemesis Dreadknight"
