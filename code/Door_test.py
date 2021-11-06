import unittest

from Door import Door
from Point import P


class Wall_test(unittest.TestCase):

    def test_0_create_door(self):
        p1, p2 = P(0, 0), P(1,0)
        door = Door(p1, p2)
        self.assertIsInstance(door, Door)
        self.assertTrue(door.p1 == p1 and door.p2 == p2)

    def test_1_create_door_error(self):
        with self.assertRaises(AssertionError):
            Door(P(0, 0), (1,0))
        with self.assertRaises(AssertionError):
            Door([0, 0], (1,0))
            

if __name__ == '__main__':
    unittest.main()
