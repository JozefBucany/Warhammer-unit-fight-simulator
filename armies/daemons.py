class Base40k():
    def __init__(self, cover: bool = False, stealth = False, chan = False, flux = False, flam = False, fate = False,
    blmas = False, skmas = False, sktak = False, epitome = False, syll = False, trance = False, pox = False, slop = False, spoil = False, horti = False):
        self.cover = 0
        self.minushit=False
        self.crit_h_on = 6
        self.crit_w_on = 6
        self.kw = ["chaos","daemon"]
        if cover:
            self.cover = 1
        self.stealth = 0
        if stealth:
            self.stealth = 1
        self.fortyk = True
        self.aos = False
        self.fnp = 7
        self.fnpm = 7
        self.fnpp = 7
        self.chan = False
        self.flux = False
        self.flam = False
        self.fate = False
        if chan:
            self.chan = True
        if flux:
            self.flux = True
        if flam:
            self.flam = True
        if fate:
            self.fate = True
        self.skmas = False
        self.blmas = False
        self.sktak = False
        if skmas:
            self.skmas = True
        if blmas:
            self.blmas = True
        if sktak:
            self.sktak = True
        self.epitome = False
        self.syll = False
        self.trance = False
        if epitome:
            self.epitome = True
        if syll:
            self.syll = True
        if trance:
            self.trance = True
        self.slop = False
        self.spoil = False
        self.pox = False
        self.horti = False
        if slop:
            self.slop = True
        if spoil:
            self.spoil = True
        if pox:
            self.pox = True
        if horti:
            self.horti = True

    def __repr__(self):
        x = "================================================================\n"
        x += f"{self.name}:\n"
        x+= "================================================================\n"
        x += f"Toughness: {self.toughness}\n"
        if self.save < 7:
            x += f"armor save: {self.save}\n"
        if self.invul < 7:
            x+= f"Invulnerable save: {self.invul}\n"
        if self.fnp <7:
            x+= f"Feel no pain: {self.fnp}"
        if self.cover == 0:
            x += "in cover? = No\n"
        else:
            x += "in cover? = Yes\n"
        if self.chan:
            x += "led by Changecaster\n"
        if self.flux:
            x += "led by Fluxmaster\n"
        if self.flam:
            x += "led by Exalted Flamer\n"
        if self.fate:
            x += "led by FateSkimmer\n"
        if self.blmas:
            x += "led by Blood Master\n"
        if self.skmas:
            x += "led by Skull Master\n"
        if self.sktak:
            x += "led by Skull Taker\n"
        if self.epitome:
            x += "led by Contorted Epitome\n"
        if self.syll:
            x += "led by Syll'Esske\n"
        if self.trance:
            x += "led by TranceWeaver\n"
        if self.pox:
            x += "led by Poxbringer\n"
        if self.slop:
            x += "led by Sloppity bilepiper\n"
        if self.spoil:
            x += "led by Spoilpox Scrivener\n"
        if self.horti:
            x += "led by Horticulous Slimux\n"
        return x


class Belakor40k(Base40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Be'LaKor"
        self.kw.append("monster")
        self.kw.append("character")
        self.hp = 20
        self.models = 1
        self.toughness = 11
        self.save = 3
        self.invul = 4
        self.melee_weapons5 = [[1,7,2,14,4,"d6+1",{"strike":True, "devastating_wounds":True}],
                                [0,14,2,8,3,1,{"sweep":True, "sustained_hits":1}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,12,2,6,3,1,{"focused":True,"psychic":True, "ignore_cover":True, "hazardous":True, "devastating_wounds":True}],
                                [0,9,2,5,2,1,{"not":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True}]]
        self.ranged_weapons10 = []
        for item in self.melee_weapons5:
            item[6]["reroll_h_1"] = True
        for item in self.ranged_weapons5:
            item[6]["reroll_h_1"] = True

class DP40k(Base40k):
    def __init__(self, alegiance = None, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Daemon Prince"
        self.kw.append("monster")
        self.kw.append("character")
        self.hp = 10
        self.models = 1
        self.toughness = 10
        self.save = 2
        self.invul = 3
        self.stealth = 1
        self.melee_weapons5 = [[1,6,2,8,2,3,{"strike":True}],
                               [0,14,2,6,0,1,{"sweep":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,2,5,1,2,{}]]
        self.ranged_weapons10 = []
        match(alegiance):
            case "tzeentch":
                self.name += " of Tzeentch"
                self.ranged_weapons5[0][1] = 6
            case "khorne":
                self.name += " of Khorne"
                for item in self.melee_weapons5:
                    item[3] += 2
            case "nurgle":
                self.name += " of Nurgle"
                self.toughness += 1
            case "slaanesh":
                self.name += " of Slaanesh"
            case _:
                pass

class DPW40k(Base40k):
    def __init__(self, alegiance = None, mode = None, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Daemon Prince with wings"
        self.kw.append("monster")
        self.kw.append("character")
        self.hp = 10
        self.models = 1
        self.toughness = 9
        self.save = 2
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,8,2,3,{"strike":True}],
                               [0,14,2,6,0,1,{"sweep":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,2,5,1,2,{}]]
        self.ranged_weapons10 = []
        match(alegiance):
            case "tzeentch":
                self.name += " of Tzeentch"
                self.ranged_weapons5[0][1] = 6
            case "khorne":
                self.name += " of Khorne"
                for item in self.melee_weapons5:
                    item[3] += 2
            case "nurgle":
                self.name += " of Nurgle"
                self.toughness += 1
            case "slaanesh":
                self.name += " of Slaanesh"
            case _:
                pass
        match (mode):
            case "sustained":
                for item in self.melee_weapons5:
                    item[6]["sustained_hits"]=1
            case "lethal":
                for item in self.melee_weapons5:
                    item[6]["lethal_hits"]=True
            case _:
                pass

class SoulGrinder40k(Base40k):
    def __init__(self, weapon = None, alegiance = None, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Soul Grinder"
        self.kw.append("vehicle")
        self.kw.append("walker")
        self.hp = 14
        self.models = 1
        self.toughness = 11
        self.save = 3
        self.invul = 4
        self.melee_weapons5 = [[1,5,3,16,3,"d6+2",{}],[1,3,3,8,2,"d6",{}]]
        if weapon == "claw":
            self.melee_weapons5[1] = [1,6,3,8,1,2,{}]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,10,1,3,{}]]
        self.ranged_weapons10 = []
        match(alegiance):
            case "tzeentch":
                self.name += " of Tzeentch"
                self.ranged_weapons5.append([1,"d3",3,12,2,"d6+2",{"blast":True}])
            case "khorne":
                self.name += " of Khorne"
                self.ranged_weapons5.append([1,"2d6","torrent",5,1,1,{"ignore_cover":True}])
            case "nurgle":
                self.name += " of Nurgle"
                self.ranged_weapons5.append([1,"d6+1",3,7,1,2,{"blast":True, "lethal_hits":True}])
            case "slaanesh":
                self.name += " of Slaanesh"
                self.ranged_weapons5.append([1,6,3,9,2,2,{"sustained_hits":1,"devastating_wounds":True}])
            case _:
                pass
