from logging import raiseExceptions
import unittest

from Area import Area
from Boundary import Boundary
from Door import Door
from Point import P
from Wall import Wall


class Area_test(unittest.TestCase):

    def test_0_create_simple_area(self):
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, wall4])
        self.assertListEqual(area.walls, [wall1, wall2, wall3, wall4])

    def test_1_create_area_error(self):
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        # Only 3 dividers
        with self.assertRaises(AssertionError):
            Area('Kitchen', [wall1, wall2, wall3])
        
        # 4 dividers but not closing
        wall4 = Wall(P(10,10), P(5,10))
        with self.assertRaises(AssertionError):
            Area('Kitchen', [wall1, wall2, wall3, wall4])


    def test_2_sort_dividers(self):
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        boundary = Boundary(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, boundary])
        self.assertListEqual(area.walls, [wall1, wall2, wall3])
        self.assertListEqual(area.boundaries, [boundary])

    def test_3_sort_dividers_error(self):
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        door = Door(P(0,10), P(0,0))
        with self.assertRaises(AssertionError):
            Area('Kitchen', [wall1, wall2, wall3, door])

    def test_4_change_divider(self):
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, wall4])
        boundary = Boundary(P(0,10), P(0,0))
        area.change_divider_by_id(wall4.id, boundary)
        self.assertListEqual(area.walls, [wall1, wall2, wall3])
        self.assertListEqual(area.boundaries, [boundary])

if __name__ == '__main__':
    unittest.main()
