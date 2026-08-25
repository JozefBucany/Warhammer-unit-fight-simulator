class NDK():
    def __init__(self, meleewep:str|None=None, weapons:list[str|None]=[], cover: bool = False, stealth = False):
        self.name = "Nemesis Dreadknight"
        self.models = 1
        self.fortyk = True
        self.aos = False
        self.kw = ["psyker", "vehicle"]
        self.hp = 13
        self.fnp = 7
        self.fnpm = 7
        self.fnpp = 7
        self.cover = 0
        if cover:
            self.cover = 1
        self.stealth = 0
        if stealth:
            self.stealth = 1
        self.minushit = False
        self.toughness = 8
        self.save = 2
        self.invul = 4
        self.melee_weapons5 = [[1,6,2,6,1,1,{}]]
        self.ranged_weapons5 = []
        match (meleewep):
            case "hammer":
                self.melee_weapons5=[[1,5,3,14,3,"d6+1",{"psychic": True}]]
            case "flail":
                self.melee_weapons5=[[1,10,2,5,1,2,{"psychic": True}]]
            case "mace":
                self.melee_weapons5=[[1,5,2,6,3,3,{"anti_character": 2, "psychic": True}]]
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

    def __repr__(self):
        x = f"{self.name}"
        x+=":\n"
        x += f"Toughness: {self.toughness}\n"
        x += f"Invulnerable save: {self.invul}\n"
        if self.cover == 0:
            x += "in cover? = No"
        else:
            x += "in cover? = Yes"
        x += "\n"
        return x

class GMNDK(NDK):
    def __init__(self, meleewep:str|None=None, weapons:list[str|None]=[], cover: bool = False, stealth = False):
        super().__init__(meleewep, weapons, cover,stealth)
        self.kw.append("character")
        self.name = "Grandmaster is Nemesis Dreadknight"
