from Wall import Wall
from Boundary import Boundary

class Area():
    
    id = 0

    def __init__(self, name, dividers = []):
        self.id = Area.id
        Area.id += 1
        self.name = name
        self.walls = []
        self.boundaries = []
        self.__add_dividers(dividers)
        
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __add_dividers(self, dividers):
        assert isinstance(dividers, (list, tuple))
        if len(dividers)>0:
            for elem in dividers:
                assert isinstance(elem, Wall) or isinstance(elem, Boundary), "Neither a Wall nor a Boundary"
                if isinstance(elem, Wall):
                    self.walls.append(elem)
                if isinstance(elem, Boundary):
                    self.boundaries.append(elem)

    def get_corners(self):
        assert len(self.walls)+len(self.boundaries) == 4, 'To get corners, an area must have 4 walls/boundaries'
        x_min = min(min(wall.get_x_coords() for wall in self.walls), min(boundary.get_x_coords() for boundary in self.boundaries))
        x_max = max(max(wall.get_x_coords() for wall in self.walls), max(boundary.get_x_coords() for boundary in self.boundaries))
        y_min = min(min(wall.get_y_coords() for wall in self.walls), min(boundary.get_y_coords() for boundary in self.boundaries))
        y_max = max(max(wall.get_y_coords() for wall in self.walls), max(boundary.get_y_coords() for boundary in self.boundaries))
        return (x_min, x_max, y_min, y_max)


