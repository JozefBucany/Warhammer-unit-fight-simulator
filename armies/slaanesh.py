from armies.daemons import Base40k


class Slaanesh40k(Base40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome = epitome, syll = syll, trance = trance)
        self.kw.append("slaanesh")

class Daemonettes40k (Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome=epitome, syll=syll, trance=trance)
        self.name = "Slaanesh Daemonettes"
        self.kw.append("infantry")
        self.hp = 1
        self.models = 10
        self.toughness = 3
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[10,3,3,4,1,1,{"devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if epitome:
            self.kw.append("character")
            self.fnpm = 4
            self.melee_weapons5.append([1,8,2,4,1,1,{"devastating_wounds":True}])
            self.melee_weapons5.append([1,"d6",4,5,1,2,{}])
        if syll:
            self.kw.append("character")
            self.crit_w_on = 5
            self.melee_weapons5.append([1,6,3,7,2,3,{}])
            self.melee_weapons5.append([1,6,2,4,1,1,{}])
            self.ranged_weapons5 = [[1,"2d6","torrent",6,1,1,{"focused":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True, "hazardous":True}],
                                    [0,"d6", "torrent",6,1,1,{"not":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True}],
                                    [1,6,3,4,1,1,{}]]
        if trance:
            self.kw.append("character")
            self.melee_weapons5.append([1,6,2,4,1,1,{"devastating_wounds":True}])
            for item in self.melee_weapons5:
                item[6]["oath"]=True

class Fiends40k (Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Fiends of Slaanesh"
        self.kw.append("beast")
        self.models = 3
        self.hp = 4
        self.toughness = 5
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[3,5,3,5,2,2,{"devastating_wounds":True}]]
        self.melee_weapons10 = [[3,5,3,5,2,2,{"devastating_wounds":True}]]
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Seekers40k (Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Seekers of Slaanesh"
        self.kw.append("mounted")
        self.models = 5
        self.hp = 2
        self.toughness = 4
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[5,2,4,4,0,1,{"lethal_hits":True}],[5,3,3,4,1,1,{"devastating_wounds":True}]]
        self.melee_weapons10 = [[5,2,4,4,0,1,{"lethal_hits":True}],[5,3,3,4,1,1,{"devastating_wounds":True}]]
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Hellflayer40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Slaanesh Hellflayer"
        self.kw.append("mounted")
        self.models = 1
        self.hp = 7
        self.toughness = 6
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,3,3,5,1,3,{"anti-infantry":3}],[1,4,4,5,0,2,{"lethal_hits":True}],[1,8,3,5,1,2,{"devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,3,3,4,1,2,{"anti-infantry":3}]]
        self.ranged_weapons10 = []

class TranceWeaver40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, trance=False):
        super().__init__(cover, stealth, trance=trance)
        self.name = "Tranceweaver"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 3
        self.toughness = 3
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[1,6,2,4,1,1,{"devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if trance:
            self.melee_weapons5[0][6]["oath"]=True


class Epitome40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False):
        super().__init__(cover, stealth, epitome=epitome)
        self.name = "Contorted Epitome"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        if epitome:
            self.fnpm = 4
        self.hp = 8
        self.toughness = 6
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,8,2,4,1,1,{"devastating_wounds":True}],[1,"d6",4,5,1,2,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Enrapturess40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Infernal Enrapturess"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 3
        self.toughness = 3
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[1,5,2,4,1,1,{"devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[0,6,3,6,0,1,{"not":True}],[1,1,3,12,3,"d6+1",{"focused":True}]]
        self.ranged_weapons10 = []

class Syllesske40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, syll = False):
        super().__init__(cover, stealth, syll=syll)
        self.name = "Syll'Esske"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 9
        self.toughness = 6
        if syll:
            self.crit_w_on = 5
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,6,3,7,2,3,{}],[1,6,2,4,1,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"2d6","torrent",6,1,1,{"focused":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True, "hazardous":True}],
                                [0,"d6", "torrent",6,1,1,{"not":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True}],
                                [1,6,3,4,1,1,{}]]
        self.ranged_weapons10 = []

class Keeper40k(Slaanesh40k):
    def __init__(self, weapon = None, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Keeper of Secrets"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.minushit = True
        self.hp = 18
        self.toughness = 10
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,8,3,3,{}],[1,4,2,6,3,3,{"devastating_wounds":True}]]
        self.ranged_weapons5 = [[1,9,2,6,2,1,{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}],
                                [0,6,2,6,2,1,{"not":True, "psychic":True, "devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons10 = []
        match(weapon):
            case "whip":
                self.ranged_weapons5.append([1,6,2,6,1,2,{}])
            case "knife":
                self.melee_weapons5.append([1,3,2,6,3,2,{}])
            case "shield":
                self.save = 3
            case _:
                pass

class Shalaxi40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Shalaxi Helbane"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 20
        self.toughness = 10
        self.save = 3
        self.invul = 4
        self.melee_weapons5 = [[1,4,2,6,2,3,{"devastating_wounds":True}],[1,6,2,12,3,"d6+2",{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"d6",2,9,2,"d3",{"focused":True, "hazardous":True, "devastating_wounds":True, "psychic":True, "sustained_hits":"d3"}],
                                [0,"d6",2,9,1,"d3",{"not":True, "devastating_wounds":True, "psychic":True}],[1,6,2,6,1,2,{}]]
        self.ranged_weapons10 = []
