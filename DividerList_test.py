import unittest
from DividerList import DividerList
from Wall import Wall

class DividerList_test(unittest.TestCase):

    def test_create_walllist(self):
        divider_list = DividerList()
        self.assertIsInstance(divider_list, DividerList)
    
    def test_create_empty_walllist(self):
        divider_list = DividerList([])
        self.assertEqual(divider_list.list, [])
    
    def test_create_single_wall_walllist(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        wall = Wall((x1, y1), (x2, y2))
        divider_list = DividerList([wall])
        self.assertEqual(divider_list.list, [wall])

    def test_create_two_wall_walllist(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        wall1 = Wall((x1, y1), (x2, y2))
        wall2 = Wall((x1, y1), (x2, y2))
        divider_list = DividerList([wall1, wall2])
        self.assertEqual(divider_list.list, [wall1, wall2])

    

if __name__ == '__main__':
    unittest.main()