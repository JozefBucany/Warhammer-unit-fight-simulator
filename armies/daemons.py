class Base40k():
    def __init__(self, cover: bool = False, stealth = False):
        self.cover = 0
        self.minushit=False
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
