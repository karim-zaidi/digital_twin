import unittest
from Wall import Wall
from WallList import WallList
from Room import Room


class Room_test(unittest.TestCase):

    def test_create_simple_room(self):
        wall1 = Wall((0, 0), (10,0))
        wall2 = Wall((10, 0), (10,10))
        wall3 = Wall((10,10), (0,10))
        wall4 = Wall((0,10), (0,0))
        wall_list = WallList([wall1, wall2, wall3, wall4])
        room = Room(wall_list)
        self.assertIsInstance(room, Room)


if __name__ == '__main__':
    unittest.main()