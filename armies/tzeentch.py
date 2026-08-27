from armies.daemons import Base40k


class Tzeentch40k(Base40k):
    def __init__(self, cover: bool = False, stealth = False, chan=False, flux= False, flam=False, fate = False):
        super().__init__(cover, stealth, chan = chan, flux = flux, flam = flam, fate = fate)
        self.kw.append("tzeentch")

class PHorrors40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, chan=False, flux= False):
        super().__init__(cover, stealth, chan=chan, flux=flux)
        self.name = "Pink Horrors of Tzeentch"
        self.kw.append("infantry")
        self.hp = 1
        self.models = 10
        self.toughness = 3
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[10,1,4,3,0,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[10,2,3,4,1,1,{"psychic":True}]]
        self.ranged_weapons10 = []
        if chan:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.ranged_weapons5.append([1,3,3,6,2,"d3",{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}])
            self.ranged_weapons5.append([0,3,3,5,1,"d3",{"not":True, "psychic":True}])
            for item in self.ranged_weapons5:
                item[6]["sustained_hits"]=1
        if flux:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.ranged_weapons5.append([1,3,3,6,2,"d3",{"psychic":True,"focused":True,"hzardous":True,"devastating_wounds":True}])
            self.ranged_weapons5.append([0,3,3,5,1,"d3",{"psychic":True,"not":True}])
            self.minushit = True

class BB1Horrors40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, chan=False, flux= False):
        super().__init__(cover, stealth, chan=chan, flux=flux)
        self.name = "Blue Horrors of Tzeentch"
        self.kw.append("infantry")
        self.hp = 1
        self.models = 10
        self.toughness = 3
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[10,1,5,3,0,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[10,2,4,3,1,1,{"psychic":True}]]
        self.ranged_weapons10 = []
        if chan:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.ranged_weapons5.append([1,3,3,6,2,"d3",{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}])
            self.ranged_weapons5.append([0,3,3,5,1,"d3",{"not":True, "psychic":True}])
            for item in self.ranged_weapons5:
                item[6]["sustained_hits"]=1
        if flux:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.ranged_weapons5.append([1,3,3,6,2,"d3",{"psychic":True,"focused":True,"hzardous":True,"devastating_wounds":True}])
            self.ranged_weapons5.append([0,3,3,5,1,"d3",{"psychic":True,"not":True}])
            self.minushit = True

class BB2Horrors40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, chan=False, flux= False):
        super().__init__(cover, stealth, chan=chan, flux=flux)
        self.name = "Brimstone Horrors of Tzeentch"
        self.kw.append("infantry")
        self.hp = 1
        self.models = 10
        self.toughness = 3
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[10,2,5,2,0,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[10,2,5,2,1,1,{"psychic":True}]]
        self.ranged_weapons10 = []
        if chan:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.ranged_weapons5.append([1,3,3,6,2,"d3",{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}])
            self.ranged_weapons5.append([0,3,3,5,1,"d3",{"not":True, "psychic":True}])
            for item in self.ranged_weapons5:
                item[6]["sustained_hits"]=1
        if flux:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.ranged_weapons5.append([1,3,3,6,2,"d3",{"psychic":True,"focused":True,"hzardous":True,"devastating_wounds":True}])
            self.ranged_weapons5.append([0,3,3,5,1,"d3",{"psychic":True,"not":True}])
            self.minushit = True

class Flamers40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, flam = False):
        super().__init__(cover, stealth, flam = flam)
        self.name = "Flamers of Tzeentch"
        self.kw.append("infantry")
        self.hp = 3
        self.models = 3
        self.toughness = 4
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[3,3,4,4,0,1,{}]]
        self.melee_weapons10 = [[3,3,4,4,0,1,{}]]
        self.ranged_weapons5 = [[3,"d6","torrent",4,1,1,{"psychic":True,"ignore_cover":True}]]
        self.ranged_weapons10 = [[3,"d6","torrent",4,1,1,{"psychic":True,"ignore_cover":True}]]
        if flam:
            self.kw.append("character")
            self.melee_weapons5.append([1,4,4,5,0,1,{}])
            self.ranged_weapons5.append([1,3,3,9,3,3,{"focused":True,"psychic":True,"ignore_cover":True}])
            self.ranged_weapons5.append([0,"2d6","torrent",5,1,1,{"not":True,"psychic":True,"ignore_cover":True}])

class Screamers40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, fate = False):
        super().__init__(cover, stealth, fate = fate)
        self.name = "Screamers of Tzeentch"
        self.kw.append("beast")
        self.hp = 3
        self.models = 3
        self.toughness = 4
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[3,3,3,6,2,2,{"anti-vehicle":True, "anti-monster":True}]]
        self.melee_weapons10 = [[3,3,3,6,2,2,{"anti-vehicle":True, "anti-monster":True}]]
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if fate:
            self.kw.append("character")
            self.melee_weapons5.append([1,3,4,4,1,1,{"psychic":True}])
            self.melee_weapons5.append([1,6,3,6,2,2,{"anti-vehicle":True, "anti-monster":True}])
            self.ranged_weapons5 = [[1,3,3,6,2,"d3",{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}],
                                [0,3,3,5,1,"d3",{"not":True, "psychic":True}]]
            for item in self.melee_weapons5:
                item[6]["lethal_hits"] = True
            for item in self.melee_weapons10:
                item[6]["lethal_hits"] = True

class Chariot40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Burning Chariot"
        self.kw.append("infantry")
        self.hp = 9
        self.models = 1
        self.toughness = 8
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[1,6,4,5,0,1,{}],[1,6,3,6,2,2,{"anti-vehicle":True, "anti-monster":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,9,3,3,{"focused":True,"psychic":True,"ignore_cover":True}],[0,"2d6","torrent",5,1,1,{"not":True,"psychic":True,"ignore_cover":True}]]
        self.ranged_weapons10 = []

class Changecaster40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, chan = False):
        super().__init__(cover, stealth, chan = chan)
        self.name = "Changecaster"
        self.kw.append("infantry")
        self.kw.append("character")
        self.hp = 3
        self.models = 1
        self.toughness = 3
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,3,4,4,1,1,{"psychic":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,6,2,"d3",{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}],
                                [0,3,3,5,1,"d3",{"not":True, "psychic":True}]]
        self.ranged_weapons10 = []
        if chan:
            for item in self.ranged_weapons5:
                item[6]["sustained_hits"]=1

class Fluxmaster40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, flux = False):
        super().__init__(cover, stealth, flux = flux)
        self.name = "Fluxmaster"
        self.kw.append("mounted")
        self.kw.append("character")
        self.hp = 4
        self.models = 1
        self.toughness = 4
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,3,4,4,1,1,{"psychic":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,6,2,"d3",{"psychic":True,"focused":True,"hzardous":True,"devastating_wounds":True}],
                                [0,3,3,5,1,"d3",{"psychic":True,"not":True}]]
        self.ranged_weapons10 = []
        if flux:
            self.minushit = True

class Exaflam40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Exalted Flamer of Tzeentch"
        self.kw.append("infantry")
        self.kw.append("character")
        self.hp = 6
        self.models = 1
        self.toughness = 4
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[1,4,4,5,0,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,9,3,3,{"focused":True,"psychic":True,"ignore_cover":True}],[0,"2d6","torrent",5,1,1,{"not":True,"psychic":True,"ignore_cover":True}]]
        self.ranged_weapons10 = []

class Fateskimmer40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False, fate = False):
        super().__init__(cover, stealth, fate=fate)
        self.name = "FateSkimmer"
        self.kw.append("mounted")
        self.hp = 3
        self.models = 1
        self.toughness = 4
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,3,4,4,1,1,{"psychic":True}],[1,6,3,6,2,2,{"anti-vehicle":True, "anti-monster":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,6,2,"d3",{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}],
                                [0,3,3,5,1,"d3",{"not":True, "psychic":True}]]
        self.ranged_weapons10 = []
        if fate:
            for item in self.melee_weapons5:
                item[6]["lethal_hits"] = True

class LoC40k(Tzeentch40k):
    def __init__(self, weapon = None, mode:str=None, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Lord of Change"
        self.kw.append("monster")
        self.kw.append("character")
        self.hp = 18
        self.models = 1
        self.toughness = 10
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,5,3,6,1,3,{"psychic":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,9,2,10,2,3,{"psychic":True, "hazardous":True,"focused":True}],
                                [0,9,2,10,1,1,{"psychic":True, "not":True}]]
        self.ranged_weapons10 = []
        match (weapon):
            case "sword":
                self.melee_weapons5.append([1,3,3,7,2,3,{}])
            case "rod":
                self.ranged_weapons5.append([1,6,2,9,1,2,{"psychic":True}])
            case _:
                pass
        match(mode):
            case "sustain":
                self.ranged_weapons5[0][6]["sustained_hits"] = "d3"
                self.ranged_weapons5[1][6]["sustained_hits"] = "d3"
            case "lethal":
                self.ranged_weapons5[0][6]["lethal_hits"] = True
                self.ranged_weapons5[1][6]["lethal_hits"] = True
            case "ignore":
                self.ranged_weapons5[0][6]["ignore_cover"] = True
                self.ranged_weapons5[1][6]["ignore_cover"] = True
            case _:
                pass

class Kairos40k(Tzeentch40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Kairos Fateweaver"
        self.kw.append("monster")
        self.kw.append("character")
        self.hp = 20
        self.models = 1
        self.toughness = 10
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,5,3,8,2,"2d3",{"psychic":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"d3+6",2,9,2,3,{"psychic":True, "hazardous":True,"focused":True,"blast":True}],
                                [0,"d6+3",2,9,2,"d3",{"psychic":True, "not":True, "blast":True}]]
        self.ranged_weapons10 = []
