from Point import P


class Element():

    __id = 0

    def __init__(self, p1, p2):
        assert isinstance(p1,P), f'p1 must be a P (point), not a {type(p1).__name__}'
        assert isinstance(p2,P), f'p2 must be a P (point), not a {type(p2).__name__}'
        self.__p1 = p1
        self.__p2 = p2
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
        assert isinstance(new_p1,P), f'p1 must either be a P (point), not a {type(new_p1).__name__}'
        self.__p1 = new_p1
        assert self.is_axis_aligned(), 'An element must either be aligned with the x or the y axis'


    # p2
    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, new_p2):
        assert isinstance(new_p2,P), f'p1 must either be a P (point), not a {type(new_p2).__name__}'
        self.__p2 = new_p2
        assert self.is_axis_aligned(), 'An element must either be aligned with the x or the y axis'


    # Other methods
    def get_x_coords(self):
        """Return the coordinates on the x axis in ascending order"""
        return min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x)


    def get_y_coords(self):
        """Return the coordinates on the y axis in ascending order"""
        return min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y)


    def is_axis_aligned(self):
        return self.p1.x == self.p2.x or self.p1.y == self.p2.y

    
    @staticmethod
    def coincide(e1,e2):
        """Returns if the two elements define the same segment on the plane (ie if their points are the same, their order notwithstanding)"""
        assert isinstance(e1,Element) and isinstance(e2,Element)
        return (P.equal(e1.p1,e2.p1) and P.equal(e1.p2,e2.p2)) \
            or (P.equal(e1.p1,e2.p2) and P.equal(e1.p2,e2.p1))

