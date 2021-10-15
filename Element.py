class Element():

    id = 0

    def __init__(self, p1, p2):
        assert isinstance(p1, tuple) and isinstance(p2, tuple), 'The 2 coordinates points must be tuples'
        assert len(p1) == 2 and len(p2) == 2, 'Each coordinate point must have 2 coordinates'
        assert isinstance(p1[0], int) or isinstance(p1[0], float), 'Coordinates must be int of float'
        assert isinstance(p1[1], int) or isinstance(p1[1], float), 'Coordinates must be int of float'
        assert isinstance(p2[0], int) or isinstance(p2[0], float), 'Coordinates must be int of float'
        assert isinstance(p2[1], int) or isinstance(p2[1], float), 'Coordinates must be int of float'

        self.p1 = p1
        self.p2 = p2
        assert self.is_axis_aligned(), 'An element must either be aligned with the x or the y axis'

        self.id = Element.id # Each element (door, boundary(=invisible/open wall), door, window) has a unique id
        Element.id += 1

    def is_axis_aligned(self):
        return self.p1[0] == self.p2[0] or self.p1[1] == self.p2[1]

    def get_x_coords(self):
        return (self.p1[0], self.p2[0])

    def get_y_coords(self):
        return (self.p1[1], self.p2[1]) 