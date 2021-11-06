import unittest

from Door import Door
from Point import P


class Door_test(unittest.TestCase):

    def test_0_create_door(self):
        p1, p2 = P(0, 0), P(1,0)
        door = Door(p1, p2)
        self.assertIsInstance(door, Door)
        self.assertEqual(door.p1, p1)
        self.assertEqual(door.p2, p2)


    def test_1_create_door_error(self):
        with self.assertRaises(AssertionError):
            Door(P(0, 0), (1,0))
        with self.assertRaises(AssertionError):
            Door([0, 0], (1,0))
            

    def test_2_attribut(self):
        p1, p2 = P(0, 0), P(1,0)
        door = Door(p1, p2)
        
        # changing attribut
        new_p1, new_p2 = P(2,0), P(10,0)
        door.p1, door.p2 = new_p1, new_p2
        self.assertEqual(door.p1, new_p1)
        self.assertEqual(door.p2, new_p2)


    def test_3_attribut_error(self):
        p1, p2 = P(0, 0), P(1,0)
        door = Door(p1, p2)
        
        # p1
        with self.assertRaises(AttributeError):
            door.__p1
        
        # p2
        with self.assertRaises(AttributeError):
            door.__p2


if __name__ == '__main__':
    unittest.main()
