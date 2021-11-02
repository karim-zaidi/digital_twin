from Wall import Wall
from Boundary import Boundary
from Point import P
from Element import Element

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

    
    def is_valid_area(self):
        """Returns if the dividers of the area define a non flat rectangle.
        Done by checking if the 4 dividers are equal to the sides of the bounding box of the area"""
        dividers = self.walls + self.boundaries
        assert len(dividers) == 4, 'To be valid, an area must have exactly 4 dividers'

        x_min, x_max, y_min, y_max = self.__get_bounding_box

        # First making sure the area is not flat along the x or y axis
        # Done by checking if a value repeats in (x_min, x_max, y_min, y_max)
        l = (x_min, x_max, y_min, y_max)
        if len(set(l))<len(l):
            return False

        # North divider
        N_div = Element(P(x_min,y_max),P(x_max,y_max))
        if not any(Element.coincide(N_div,div) for div in dividers):
            return False

        # East divider
        E_div = Element(P(x_max,y_min),P(x_max,y_max))
        if not any(Element.coincide(E_div,div) for div in dividers):
            return False

        # West divider
        W_div = Element(P(x_min,y_min),P(x_min,y_max))
        if not any(Element.coincide(W_div,div) for div in dividers):
            return False

        # South divider
        S_div = Element(P(x_min,y_min),P(x_max,y_min))
        if not any(Element.coincide(S_div,div) for div in dividers):
            return False

        return True


    def __get_bounding_box(self):
        x_min = min(x for div in self.walls+self.boundaries for x in div.get_x_coords())
        x_max = max(x for div in self.walls+self.boundaries for x in div.get_x_coords())
        y_min = min(x for div in self.walls+self.boundaries for x in div.get_y_coords())
        y_max = max(x for div in self.walls+self.boundaries for x in div.get_y_coords())
        return (x_min, x_max, y_min, y_max)

    
    def get_corners(self):
        assert self.is_valid_area()
        return self.__get_bounding_box