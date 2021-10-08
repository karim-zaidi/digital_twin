import unittest
from Window import Window

class Window_test(unittest.TestCase):

    def test_create_window(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        window = Window((x1, y1), (x2, y2))
        self.assertIsInstance(window, Window)
        self.assertEqual(window.p1, (x1, y1))
        self.assertEqual(window.p2, (x2, y2))

if __name__ == '__main__':
    unittest.main()