from Wall import Wall
from Boundary import Boundary

class Area():
    
    __id = 0

    def __init__(self, name, dividers = []):
        assert len(dividers) == 4, 'An Area must have 4 dividers (ie a total of 4 walls/boundaries'
        # TODO assert is_valid ie the 4 dividers define a rectangle
        self.__id = Area.__id
        Area.__id += 1
        self.__name = name
        self.__walls = []
        self.__boundaries = []
        self.__add_dividers(dividers)
        
   
    # id
    @property
    def id(self):
        return self.__id


    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, int)
        self.__name = new_name


    # walls
    @property
    def walls(self):
        return self.__walls


    # boundaries
    @property
    def boundaries(self):
        return self.__boundaries


    # Methods
    def __add_dividers(self, dividers):
        assert isinstance(dividers, (list, tuple))
        for elem in dividers:
            assert isinstance(elem, Wall) or isinstance(elem, Boundary), "Neither a Wall nor a Boundary"
            if isinstance(elem, Wall):
                self.walls.append(elem)
            if isinstance(elem, Boundary):
                self.boundaries.append(elem)


    def get_corners(self):
        # TODO: replace following assert with assert(self.is_valid) when is_valid is done
        assert len(self.walls)+len(self.boundaries) == 4, 'To get corners, an area must have 4 walls/boundaries'
        x_min = min(x for div in self.walls+self.boundaries for x in div.get_x_coords())
        x_max = max(x for div in self.walls+self.boundaries for x in div.get_x_coords())
        y_min = min(x for div in self.walls+self.boundaries for x in div.get_y_coords())
        y_max = max(x for div in self.walls+self.boundaries for x in div.get_y_coords())
        return (x_min, x_max, y_min, y_max)


