from Wall import Wall
from Boundary import Boundary
from Point import P
from Element import Element

class Area():
    
    __id = 0

    def __init__(self, name, dividers = []):
        assert len(dividers) == 4, f'To be valid, an area must have exactly 4 dividers, not {len(dividers)}'

        self.__name = name

        self.__walls = []
        self.__boundaries = []
        self.__add_dividers(dividers)
        self.__dividers = self.walls + self.boundaries

        assert self.is_valid_area()

        self.__id = Area.__id
        Area.__id += 1

   
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
        assert isinstance(new_name, (int,str))
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

        for e in dividers:
            assert isinstance(e, Wall) or isinstance(e, Boundary), f"Divider must be a wall or a boundary, not a {type(e).__name__}"
            
            if isinstance(e, Wall):
                self.walls.append(e)
            
            if isinstance(e, Boundary):
                self.boundaries.append(e)

    
    def is_valid_area(self):
        """Returns if the dividers of the area define a non flat rectangle.
        Done by checking if the 4 dividers are equal to the sides of the bounding box of the area"""

        x_min, x_max, y_min, y_max = self.get_bounding_box()
        # First making sure the area is not flat along the x or y axis
        if x_min == x_max or y_min == y_max :
            return False

        # North divider
        N_div = Element(P(x_min,y_max),P(x_max,y_max))
        if not any(Element.coincide(N_div,div) for div in self.__dividers):
            return False

        # East divider
        E_div = Element(P(x_max,y_min),P(x_max,y_max))
        if not any(Element.coincide(E_div,div) for div in self.__dividers):
            return False

        # West divider
        W_div = Element(P(x_min,y_min),P(x_min,y_max))
        if not any(Element.coincide(W_div,div) for div in self.__dividers):
            return False

        # South divider
        S_div = Element(P(x_min,y_min),P(x_max,y_min))
        if not any(Element.coincide(S_div,div) for div in self.__dividers):
            return False

        return True


    def get_bounding_box(self):
        X = [x for div in self.__dividers for x in div.get_x_coords()]
        Y = [y for div in self.__dividers for y in div.get_y_coords()]
        return (min(X), max(X), min(Y), max(Y))
    

    def __get_divider_by_id(self, id):
        for d in self.__dividers:
            if d.id == id:
                return d
        raise ValueError(f'There is no divider with such an id on this ({self.id}) area')


    def change_divider_by_id(self, id, divider):
        d = self.__get_divider_by_id(id)
        if Element.coincide(d,divider):
            if isinstance(d, Wall) and isinstance(divider, Boundary):
                self.walls.remove(d)
                self.boundaries.append(divider)
            elif isinstance(d, Boundary) and isinstance(divider, Wall):
                self.boundaries.remove(d)
                self.walls.append(divider)