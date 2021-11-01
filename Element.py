class Element():

    __id = 0

    def __init__(self, p1, p2):
        assert isinstance(p1, (tuple,list)), f'p1 must be either a tuple or a list not a {type(p1).__name__}'
        assert isinstance(p2, (tuple,list)), f'p2 must be either a tuple or a list not a {type(p2).__name__}'
        assert len(p1) == 2 and len(p2) == 2, 'Each coordinate point must have 2 coordinates'
        assert isinstance(p1[0], (int, float)), 'Coordinates must be int of float'
        assert isinstance(p1[1], (int, float)), 'Coordinates must be int of float'
        assert isinstance(p2[0], (int, float)), 'Coordinates must be int of float'
        assert isinstance(p2[1], (int, float)), 'Coordinates must be int of float'

        self.__p1 = tuple(p1)
        self.__p2 = tuple(p2)
        assert self.is_axis_aligned(), 'An element must either be aligned with the x or the y axis'

        # Each element (door, boundary(=invisible/open wall), door, window) has a unique unchanged id
        self.__id = Element.__id
        Element.__id += 1

    # id
    @property
    def id(self):
        return self.__id

    # p1
    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, new_p1):
        assert isinstance(new_p1, (tuple,list)), f'p1 must either be a tuple or a list but not a {type(new_p1).__name__}'
        assert len(new_p1) == 2, f'p1 must have 2 coordinates, not {len(new_p1)}'
        assert isinstance(new_p1[0], (int, float)), f'Coordinates must be int of float {type(new_p1[0]).__name__}'
        assert isinstance(new_p1[1], (int, float)), f'Coordinates must be int of float not {type(new_p1[1]).__name__}'
        
        self.__p1 = tuple(new_p1)
        assert self.is_axis_aligned(), 'An element must either be aligned with the x or the y axis'

    # p2
    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, new_p2):
        assert isinstance(new_p2, (tuple, list)), f'p1 must either be a tuple or a list but not a {type(new_p2).__name__}'
        assert len(new_p2) == 2, f'p1 must have 2 coordinates, not {len(new_p2)}'
        assert isinstance(new_p2[0], (int, float)), f'Coordinates must be int of float {type(new_p2[0]).__name__}'
        assert isinstance(new_p2[1], (int, float)), f'Coordinates must be int of float not {type(new_p2[1]).__name__}'
        self.__p2 = tuple(new_p2)
        assert self.is_axis_aligned(), 'An element must either be aligned with the x or the y axis'

    # Other methods
    def get_x_coords(self):
        """Return the coordinates on the x axis in ascending order"""
        return min(self.__p1[0], self.__p2[0]), max(self.__p1[0], self.__p2[0])

    def get_y_coords(self):
        """Return the coordinates on the y axis in ascending order"""
        return min(self.__p1[1], self.__p2[1]), max(self.__p1[1], self.__p2[1])

    def is_axis_aligned(self):
        return self.__p1[0] == self.__p2[0] or self.__p1[1] == self.__p2[1]
