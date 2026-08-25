from .daemons import Base40k


class Slaanesh40k(Base40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth)
        self.kw.append("slaanesh")
        self.epitome = False
        self.syll = False
        self.trance = False
        if epitome:
            self.epitome = True
        if syll:
            self.syll = True
        if trance:
            self.trance = True

    def __repr__(self):
        x = "================================\n"
        x += f"{self.name}:\n"
        x+= "================================\n"
        x += f"Toughness: {self.toughness}\n"
        if self.invul < 7:
            x+= f"Invulnerable save: {self.invul}\n"
        if self.fnp <7:
            x+= f"Feel no pain: {self.fnp}"
        if self.cover == 0:
            x += "in cover? = No\n"
        else:
            x += "in cover? = Yes\n"
        if self.epitome:
            x += "led by Contorted Epitome\n"
        if self.syll:
            x += "led by Syll'Esske\n"
        if self.trance:
            x += "led by TranceWeaver\n"
        return x


class Daemonettes40k (Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
        self.name = "Slaanesh Daemonettes"
        self.kw.append("infantry")
        self.hp = 1
        self.models = 10
        self.toughness = 3
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[10,3,3,4,1,1,{"devastating_wounds":True}]]
        self.melee_weapons10 = [[10,3,3,4,1,1,{"devastating_wounds":True}]]
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
        if epitome:
            self.kw.append("character")
            self.fnpm = 4
            self.melee_weapons5.append([1,8,2,4,1,1,{"devastating_wounds":True}])
            self.melee_weapons5.append([1,"d6",4,5,1,2,{}])
        if syll:
            self.kw.append("character")
            #crit wounds on 5+
            self.melee_weapons5.append([1,6,3,7,2,3,{}])
            self.melee_weapons5.append([1,6,2,4,1,1,{}])
            self.ranged_weapons5 = [[1,"2d6","torrent",6,1,1,{"focused":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True, "hazardous":True}],
                                    [0,"d6", "torrent",6,1,1,{"not":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True}],
                                    [1,6,3,4,1,1,{}]]
        if trance:
            self.kw.append("character")
            # full reroll hits
            self.melee_weapons5.append([1,6,2,4,1,1,{"devastating_wounds":True}])

class Fiends40k (Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
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
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
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
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
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
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
        self.name = "Tranceweaver"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 3
        if trance:
            pass # full reroll hits
        self.toughness = 3
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[1,6,2,4,1,1,{"devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Epitome40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
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
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
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
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
        self.name = "Syll'Esske"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 9
        self.toughness = 6
        if syll:
            pass #crit wounds on 5+
        self.save = 6
        self.invul = 4
        self.melee_weapons5 = [[1,6,3,7,2,3,{}],[1,6,2,4,1,1,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"2d6","torrent",6,1,1,{"focused":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True, "hazardous":True}],
                                [0,"d6", "torrent",6,1,1,{"not":True, "psychic":True, "ignore_cover":True, "devastating_wounds":True}],
                                [1,6,3,4,1,1,{}]]
        self.ranged_weapons10 = []

class Keeper40k(Slaanesh40k):
    def __init__(self, weapons: str = None, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
        self.name = "Keeper of Secrets"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.minushit = True
        self.hp = 18
        self.toughness = 10
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,8,2,3,{}],[1,4,2,6,2,3,{"devastating_wounds":True}]]
        self.ranged_weapons5 = [[1,9,2,6,2,1,{"focused":True, "psychic":True, "hazardous":True, "devastating_wounds":True}],
                                [0,6,2,6,2,1,{"not":True, "psychic":True, "devastating_wounds":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons10 = []
        match(weapons):
            case "whip":
                self.ranged_weapons5.append([1,6,2,6,1,2,{}])
            case "knife":
                self.melee_weapons5.append([1,3,2,6,2,2,{}])
            case "shield":
                self.save = 3
            case _:
                pass

class Shalaxi40k(Slaanesh40k):
    def __init__(self, cover: bool = False, stealth = False, epitome=False, syll = False, trance=False):
        super().__init__(cover, stealth, epitome, syll, trance)
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
