import unittest
from Area import Area
from Wall import Wall
from DividerList import DividerList
from Boundary import Boundary
from Door import Door

class Area_test(unittest.TestCase):

    def test_create_empty_area(self):
        area = Area('Kitchen', DividerList([]))
        self.assertIsInstance(area, Area)

    def test_create_simple_area(self):
        wall1 = Wall((0, 0), (10,0))
        wall2 = Wall((10, 0), (10,10))
        wall3 = Wall((10,10), (0,10))
        wall4 = Wall((0,10), (0,0))
        divider_list = DividerList([wall1, wall2, wall3, wall4])
        area = Area('Kitchen', divider_list)
        self.assertListEqual(area.walls, divider_list.list)

    def test_sort_dividers(self):
        wall1 = Wall((0, 0), (10,0))
        wall2 = Wall((10, 0), (10,10))
        wall3 = Wall((10,10), (0,10))
        boundary = Boundary((0,10), (0,0))
        divider_list = DividerList([wall1, wall2, wall3, boundary])
        area = Area('Kitchen', divider_list)
        self.assertListEqual(area.walls, [wall1, wall2, wall3])
        self.assertListEqual(area.boundaries, [boundary])

    def test_sort_dividers(self):
        wall1 = Wall((0, 0), (10,0))
        wall2 = Wall((10, 0), (10,10))
        wall3 = Wall((10,10), (0,10))
        door = Door((0,10), (0,0))
        divider_list = DividerList([wall1, wall2, wall3, door])
        with self.assertRaises(AssertionError):
            Area('Kitchen', divider_list)

    

if __name__ == '__main__':
    unittest.main()