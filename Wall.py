from Element import Element

class Wall(Element):

    def __init__(self, p1, p2, windows = [], doors = []):
        super().__init__(p1,p2)
        self.windows = windows
        self.doors = doors

