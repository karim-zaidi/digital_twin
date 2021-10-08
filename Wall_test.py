import unittest
from Wall import Wall

class Wall_test(unittest.TestCase):

    def test_create_wall(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        wall = Wall((x1, y1), (x2, y2))
        self.assertIsInstance(wall, Wall)
        self.assertEqual(wall.p1, (x1, y1))
        self.assertEqual(wall.p2, (x2, y2))

if __name__ == '__main__':
    unittest.main()