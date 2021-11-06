import unittest

from Point import P
from Window import Window


class Window_test(unittest.TestCase):

    def test_0_create_window(self):
        p1, p2 = P(0, 0), P(1,0)
        window = Window(p1, p2)
        self.assertIsInstance(window, Window)
        self.assertEqual(window.p1, p1)
        self.assertEqual(window.p2, p2)

    

    def test_1_create_window_error(self):
        with self.assertRaises(AssertionError):
            Window(P(0, 0), (1,0))
        with self.assertRaises(AssertionError):
            Window([0, 0], (1,0))
    
    def test_2_attribut(self):
        p1, p2 = P(0, 0), P(1,0)
        window = Window(p1, p2)
        
        # changing attribut
        new_p1, new_p2 = P(2,0), P(10,0)
        window.p1, window.p2 = new_p1, new_p2

        self.assertEqual(window.p1, new_p1)
        self.assertEqual(window.p2, new_p2)


    def test_3_attribut_error(self):
        p1, p2 = P(0, 0), P(1,0)
        window = Window(p1, p2)
        
        # p1
        with self.assertRaises(AttributeError):
            window.__p1
        
        # p2
        with self.assertRaises(AttributeError):
            window.__p2

    
if __name__ == '__main__':
    unittest.main()
