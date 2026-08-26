from armies.daemons import Base40k


class Nurgle40k(Base40k):
    def __init__(self, cover: bool = False, stealth = False, pox=False, slop= False, spoil=False, horti=False):
        super().__init__(cover, stealth, pox = pox, slop = slop, spoil = spoil, horti = horti)
        self.kw.append("nurgle")

class PlagueBearers40k (Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False, pox=False, slop= False, spoil=False):
        super().__init__(cover, stealth, pox=pox, slop=slop, spoil=spoil)
        self.name = "Nurgle PlagueBearers"
        self.kw.append("infantry")
        self.hp = 2
        self.models = 10
        self.toughness = 5
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[10,2,3,4,1,1,{"lethal_hits":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if slop:
            self.kw.append("character")
            self.melee_weapons5.append([1,4,3,5,0,1,{"lethal_hits":True}])
        if spoil:
            self.kw.append("character")
            self.melee_weapons5.append([1,6,3,5,1,1,{"lethal_hits":True}])
            for item in self.melee_weapons5:
                item[6]["sustained_hits"]=1
            self.ranged_weapons5 = [[1,"d6","torrent",3,0,1,{}]]
        if pox:
            self.kw.append("character")
            self.crit_h_on = 5
            self.melee_weapons5.append([1,4,3,5,2,2,{"lethal_hits":True}])

class Nurglings40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Nurglings"
        self.kw.append("swarm")
        self.models = 3
        self.minushit = True
        self.hp = 4
        self.toughness = 3
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[3,4,5,2,0,1,{"lethal_hits":True}]]
        self.melee_weapons10 = [[3,4,5,2,0,1,{"lethal_hits":True}]]
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Drones40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Plague Drones"
        self.kw.append("mounted")
        self.models = 3
        self.hp = 5
        self.toughness = 8
        self.save = 6
        self.invul = 5
        self.melee_weapons5 = [[3,2,4,5,1,2,{"lethal_hits":True}],[3,2,3,4,1,1,{"lethal_hits":True}]]
        self.melee_weapons10 = [[3,2,4,5,1,2,{"lethal_hits":True}],[3,2,3,4,1,1,{"lethal_hits":True}]]
        self.ranged_weapons5 = [[3,"d3",4,4,0,1,{"lethal_hits":True, "blast":True}]]
        self.ranged_weapons10 = [[3,"d3",4,4,0,1,{"lethal_hits":True, "blast":True}]]

class Beast40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False, horti=False):
        super().__init__(cover, stealth, horti)
        self.name = "Beast of Nurgle"
        self.kw.append("beast")
        self.models = 1
        self.hp = 7
        self.toughness = 9
        self.save = 6
        self.invul = 5
        self.melee_weapons5 = [[1,6,4,6,1,2,{"devastating_wounds":True}]]
        self.melee_weapons10 = [[1,6,4,6,1,2,{"devastating_wounds":True}]]
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if horti:
            self.melee_weapons5.append([1,4,3,6,2,3,{"lethal_hits":True}])
            self.melee_weapons5.append([1,2,4,7,4,3,{"lethal_hits":True, "devastating_wounds":True}])

class Sloppity40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False, slop= False):
        super().__init__(cover, stealth, slop = slop)
        self.name = "Sloppity Bilepiper"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 5
        self.toughness = 5
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[1,4,3,5,0,1,{"lethal_hits":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Spoilpox40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False, spoil=False):
        super().__init__(cover, stealth, spoil=spoil)
        self.name = "Spoilpox Scrivener"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 8
        self.toughness = 6
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,6,3,5,1,1,{"lethal_hits":True}]]
        if spoil:
            self.melee_weapons5[0][6]["sustained_hits"]=1
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"d6","torrent",3,0,1,{}]]
        self.ranged_weapons10 = []

class Poxbringer40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False, pox=False):
        super().__init__(cover, stealth, pox=pox)
        self.name = "Poxbringer"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 5
        self.toughness = 5
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[1,4,3,5,2,2,{"lethal_hits":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if pox:
            self.crit_h_on = 5

class Horti40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False, horti=False):
        super().__init__(cover, stealth, horti=horti)
        self.name = "Horticulous Slimux"
        self.kw.append("mounted")
        self.kw.append("character")
        self.models = 1
        self.hp = 10
        self.toughness = 10
        self.save = 3
        self.invul = 4
        self.melee_weapons5 = [[1,4,3,6,2,3,{"lethal_hits":True}],[1,2,4,7,4,3,{"lethal_hits":True, "devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class GUO40k(Nurgle40k):
    def __init__(self, weapons, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Great Unclean One"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 2
        self.toughness = 13
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = []
        self.ranged_weapons5 = [[1,"d6+3","torrent",5,2,1,{"ignore_cover":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons10 = []
        for item in weapons:
            match(item):
                case "sword":
                    self.melee_weapons5.append([1,6,2,10,2,"d6+1",{"strike":True, "lethal_hits":True}])
                    self.melee_weapons5.append([0,12,2,7,1,1,{"sweep":True, "lethal_hits":True}])
                case "bell":
                    self.melee_weapons5.append([1,6,2,7,1,2,{"lethal_hits":True}])
                case "flail":
                    self.ranged_weapons5.append([1,"d6+1",3,7,2,2,{}])
                case "dagger":
                    self.melee_weapons5.append([1,3,2,6,2,2,{"lethal_hits":True}])
                case _:
                    pass

class Rotigus40k(Nurgle40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Rotigus"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 22
        self.toughness = 12
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,7,2,10,3,4,{"strike":True,"psychic":True, "lethal_hits":True}],[0,14,2,8,1,2,{"sweep":True, "pychic":True,"lethal_hits":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"2d6","torrent",8,2,1,{"devastating_wounds":True, "ignore_cover":True}]]
        self.ranged_weapons10 = []
