import unittest
from Area import Area
from Wall import Wall
from WallList import WallList

class Area_test(unittest.TestCase):

    def test_create_simple_area(self):
        wall1 = Wall((0, 0), (10,0))
        wall_list = WallList([wall1])
        area = Area(wall_list)
        self.assertIsInstance(area, Area)
        self.assertEqual(area.wall_list, wall_list)

if __name__ == '__main__':
    unittest.main()