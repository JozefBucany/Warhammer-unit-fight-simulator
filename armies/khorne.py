from armies.daemons import Base40k


class Khorne40k(Base40k):
    def __init__(self, cover: bool = False, stealth = False, blmas=False, skmas = False, sktak=False):
        super().__init__(cover, stealth, blmas = blmas, skmas = skmas, sktak = sktak)
        self.kw.append("khorne")

class Bloodletters40k (Khorne40k):
    def __init__(self, cover: bool = False, stealth = False, blmas=False, sktak=False):
        super().__init__(cover, stealth, blmas=blmas, sktak=sktak)
        self.name = "Khorne Bloodletters"
        self.kw.append("infantry")
        self.hp = 1
        if sktak:
            pass
        self.models = 10
        self.toughness = 4
        self.save = 7
        self.invul = 5
        self.melee_weapons5 = [[10,2,3,5,2,2,{}]]
        if blmas:
            self.kw.append("character")
            self.melee_weapons5.append([1,5,2,6,2,3,{"lance":True}])
            self.melee_weapons5[0][6]["lance"]=True
        if sktak:
            self.kw.append("character")
            self.melee_weapons5[0][6]["devastating_wounds"] = True
            self.melee_weapons5.append([1,6,2,6,2,3,{"devastating_wounds":True, "epic_hw":True}])
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Flesh_Hounds40k (Khorne40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Flesh Hounds"
        self.kw.append("beast")
        self.models = 5
        self.hp = 2
        self.toughness = 4
        self.save = 7
        self.invul = 5
        self.fnpp = 3
        self.melee_weapons5 = [[5,3,3,5,1,1,{}]]
        self.melee_weapons10 = [[5,3,3,5,1,1,{}]]
        self.ranged_weapons5 = [[5,"d6","torrent",4,0,1,{"ignore_cover":True}]]
        self.ranged_weapons10 = [[5,"d6","torrent",4,0,1,{"ignore_cover":True}]]

class Blood_Crushers40k (Khorne40k):
    def __init__(self, cover: bool = False, stealth = False, skmas = False):
        super().__init__(cover, stealth, skmas=skmas)
        self.name = "Blood Crushers"
        self.kw.append("mounted")
        self.models = 3
        if skmas:
            pass
        self.hp = 4
        self.toughness = 7
        self.save = 3
        self.invul = 5
        self.melee_weapons5 = [[3,2,3,5,2,2,{}],[3,4,4,6,1,1,{"lance":True}]]
        self.melee_weapons10 = [[3,2,3,5,2,2,{}],[3,4,4,6,1,1,{"lance":True}]]
        if skmas:
            self.kw.append("character")
            for item in self.melee_weapons5:
                if "lance" in item[6]:
                    item[6]["devastating_wounds"] = True
            for item in self.melee_weapons10:
                if "lance" in item[6]:
                    item[6]["devastating_wounds"] = True
            self.melee_weapons5.append([1,5,2,6,2,3,{}])
            self.melee_weapons5.append([1,4,4,6,1,1,{"lance":True, "devastating_wounds":True}])
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Skull_Cannon40k(Khorne40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Skull Cannon"
        self.kw.append("mounted")
        self.models = 1
        self.hp = 9
        self.toughness = 9
        self.save = 4
        self.invul = 4
        self.melee_weapons5 = [[1,2,4,6,0,2,{}],[1,4,3,5,2,2,{}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"d6+2",3,9,1,2,{"blast":True}]]
        self.ranged_weapons10 = []

class Bloodmaster40k(Khorne40k):
    def __init__(self, cover: bool = False, stealth = False, blmas=False):
        super().__init__(cover, stealth, blmas=blmas)
        self.name = "BloodMaster"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 4
        self.toughness = 4
        self.save = 5
        self.invul = 4
        self.melee_weapons5 = [[1,5,2,6,2,3,{}]]
        if blmas:
            self.melee_weapons5[0][6]["lance"]=True
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Bloodthirster40k(Khorne40k):
    def __init__(self, weapons = None, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        match (weapons):
            case "axe+breath":
                self.melee_weapons5 = [[1,7,2,16,4,"d6+2",{"strike":True}], [0,14,2,10,2,2,{"sweep":True}]]
                self.ranged_weapons5 = [[1,"d6","torrent",5,1,1,{"ignore_cover":True}]]
            case "lash+flail":
                self.melee_weapons5 = [[1,8,2,14,4,"d3+1",{"strike":True}],[0,16,2,8,2,1,{"sweep":True}]]
                self.ranged_weapons5 = [[1,1,2,16,3,"d6+1",{"devastating_wounds":True}],[1,6,2,8,1,2,{}]]
            case _:
                self.melee_weapons5 = [[1,7,2,16,4,"d6+2",{"strike":True}], [0,14,2,10,2,2,{"sweep":True}]]
                self.ranged_weapons5 = [[1,"d6","torrent",5,1,1,{"ignore_cover":True}]]
        self.name = "Bloodthirster"
        for item in self.melee_weapons5:
            item[6]["+1_to_hit"] = True
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 18
        self.toughness = 11
        self.save = 3
        self.invul = 4
        self.melee_weapons10 = []
        self.ranged_weapons10 = []

class Karanak40k(Khorne40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Karanak"
        self.kw.append("beast")
        self.kw.append("character")
        self.models = 1
        self.hp = 5
        self.toughness = 4
        self.save = 7
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,6,2,2,{"anti-character":3}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"d6+3","torrent",5,1,1,{"ignore_cover":True}]]
        self.ranged_weapons10 = []

class Skarbrand40k(Khorne40k):
    def __init__(self, cover: bool = False, stealth = False):
        super().__init__(cover, stealth)
        self.name = "Skarbrand"
        self.kw.append("monster")
        self.kw.append("character")
        self.models = 1
        self.hp = 20
        self.toughness = 11
        self.save = 3
        self.invul = 4
        self.melee_weapons5 = [[1,9,2,16,4,6,{"strike":True}],[0,17,2,8,2,2,{"sweep":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = [[1,"2d6","torrent",8,1,1,{"ignore_cover":True}]]
        self.ranged_weapons10 = []

class Skullmaster40k(Khorne40k):
    def __init__(self, cover: bool = False, stealth = False, skmas = False):
        super().__init__(cover, stealth, skmas=skmas)
        self.name = "SkullMaster"
        self.kw.append("mounted")
        self.kw.append("character")
        self.models = 1
        self.hp = 6
        self.toughness = 7
        self.save = 3
        self.invul = 4
        self.melee_weapons5 = [[1,5,2,6,2,3,{}],[1,4,4,6,1,1,{"lance":True}]]
        if skmas:
            for item in self.melee_weapons5:
                if "lance" in item[6]:
                    item[6]["devastating_wounds"] = True
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []

class Skulltaker40k(Khorne40k):
    def __init__(self, cover: bool = False, stealth = False, sktak=False):
        super().__init__(cover, stealth, sktak=sktak)
        self.name = "SkullTaker"
        self.kw.append("infantry")
        self.kw.append("character")
        self.models = 1
        self.hp = 5
        self.toughness = 4
        self.save = 4
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,6,2,3,{"devastating_wounds":True, "epic_hw":True}]]
        self.melee_weapons10 = []
        self.ranged_weapons5 = []
        self.ranged_weapons10 = []
