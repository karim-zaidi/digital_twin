import unittest
from WallList import WallList
from Wall import Wall

class WallList_test(unittest.TestCase):

    def test_create_walllist(self):
        wall_list = WallList()
        self.assertIsInstance(wall_list, WallList)
    
    def test_create_empty_walllist(self):
        wall_list = WallList([])
        self.assertEqual(wall_list.list, [])
    
    def test_create_single_wall_walllist(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        wall = Wall((x1, y1), (x2, y2))
        wall_list = WallList([wall])
        self.assertEqual(wall_list.list, [wall])

    def test_create_two_wall_walllist(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        wall1 = Wall((x1, y1), (x2, y2))
        wall2 = Wall((x1, y1), (x2, y2))
        wall_list = WallList([wall1, wall2])
        self.assertEqual(wall_list.list, [wall1, wall2])

    

if __name__ == '__main__':
    unittest.main()