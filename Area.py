from Wall import Wall
from Boundary import Boundary

class Area():
    
    def __init__(self, name, dividers):
        self.name = name
        self.walls = []
        self.boundaries = []
        self.add_dividers(dividers.list)
    
    def add_dividers(self, dividers):
        if len(dividers)>0:
            for elem in dividers:
                assert isinstance(elem, Wall) or isinstance(elem, Boundary), "Neither a Wall nor a Boundary"
                if isinstance(elem, Wall):
                    self.walls.append(elem)
                if isinstance(elem, Boundary):
                    self.boundaries.append(elem)


