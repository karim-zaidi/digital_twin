import unittest
from Window import Window
from Point import P

class Window_test(unittest.TestCase):

    def test_0_create_window(self):
        p1, p2 = P(0, 0), P(1,0)
        window = Window(p1, p2)
        self.assertIsInstance(window, Window)
        self.assertTrue(window.p1 == p1 and window.p2 == p2)

if __name__ == '__main__':
    unittest.main()