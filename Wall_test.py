import unittest
from Wall import Wall
from Window import Window
from Door import Door

class Wall_test(unittest.TestCase):
    def setUp(self):
        self.p1, self.p2 = (0, 0), (10,0)
        self.wall = Wall(self.p1, self.p2)

    def test_0_create_simple_wall(self):
        self.assertIsInstance(self.wall, Wall)
        self.assertTrue(self.wall.p1 == self.p1 and self.wall.p2 == self.p2)
    
  
    def test_1_add_single_window(self):
        window = Window((0, 0), (1,0))
        self.wall.add_window(window)
        self.assertEqual(self.wall.windows, [window])


    def test_2_add_single_window_outside_error(self):
        """Test creating a window outside a wall"""
        window = Window((0, 0), (0,1))
        with self.assertRaises(AssertionError):
            self.wall.add_window(window)
    

    def test_3_add_single_window_size_error(self):
        """Test creating a window bigger than the wall"""
        window = Window((0, 0), (11,0))
        with self.assertRaises(AssertionError):
            self.wall.add_window(window)


    def test_4_add_multiple_windows(self):
        window1 = Window((0, 0), (1,0))
        window2 = Window((2, 0), (3,0))
        windows = [window1, window2]
        self.wall.add_window(windows)
        self.assertEqual(self.wall.windows, windows)


    def test_5_add_multiple_windows_conflict(self):
        window = Window((0, 0), (3,0))
        self.wall.add_window(window)
        with self.assertRaises(AssertionError):
            # Duplicate windows
            self.wall.add_window(window)

            # Window inside other window
            window1 = Window((1, 0), (2,0))
            self.wall.add_window(window1)
            
            # Window bigger than the other window
            window2 = Window((0, 0), (5,0))
            self.wall.add_window(window2)


    def test_6_add_door(self):
        door = Door((0, 0), (1,0))
        self.wall.add_door(door)
        self.assertEqual(self.wall.doors, [door])


    def test_7_add_single_door_outside_error(self):
        """Test creating a door outside a wall"""
        door = Door((0, 0), (0,1))
        with self.assertRaises(AssertionError):
            self.wall.add_door(door)
    

    def test_8_add_single_door_size_error(self):
        """Test creating a door bigger than the wall"""
        door = Door((-1, 0), (10,0))
        with self.assertRaises(AssertionError):
            self.wall.add_door(door)


    def test_9_add_multiple_doors(self):
        door1 = Door((0, 0), (1,0))
        door2 = Door((2, 0), (3,0))
        doors = [door1, door2]
        self.wall.add_door(doors)
        self.assertEqual(self.wall.doors, doors)


    def test_10_add_multiple_doors_conflict(self):
        door = Door((0, 0), (3,0))
        self.wall.add_door(door)
        with self.assertRaises(AssertionError):
            # Duplicate doors
            self.wall.add_window(door)

            # Door inside the other door
            door1 = Door((1, 0), (2,0))
            self.wall.add_window(door1)

            # Door bigger than ther other door
            door2 = Door((0, 0), (5,0))
            self.wall.add_window(door2)


    def test_11_add_error(self):
        with self.assertRaises(AssertionError):
            self.wall.add_window('window')
            self.wall.add_door('door')


    def test_12_conflict_window_inside_door(self):
        door = Door((0, 0), (3,0))
        window = Window((1,0), (2,0))
        self.wall.add_door(door)
        with self.assertRaises(AssertionError):
            self.wall.add_window(window)


    def test_12_conflict_door_inside_window(self):
        window = Window((0, 0), (3,0))
        door = Door((1,0), (2,0))
        self.wall.add_window(window)
        with self.assertRaises(AssertionError):
            self.wall.add_door(door)

if __name__ == '__main__':
    unittest.main()