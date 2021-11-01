import unittest
from Door import Door

class Wall_test(unittest.TestCase):

    def test_0_create_door(self):
        (x1, y1), (x2, y2) = (0, 0), (1,0)
        door = Door((x1, y1), (x2, y2))
        self.assertIsInstance(door, Door)
        self.assertTrue(door.p1 == (x1, y1) and door.p2 == (x2, y2))

if __name__ == '__main__':
    unittest.main()