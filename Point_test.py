import unittest
from Point import P


class Point_test(unittest.TestCase):

    def test_0_create_Point(self):
        self.assertIsInstance(P(0,0), P)
        self.assertIsInstance(P(1.,0), P)
    

    def test_1_create_error(self):
        with self.assertRaises(AssertionError):
            P('1', 0)


    def test_2_attribut_error(self):
        p = P(0,0)
        
        # x
        with self.assertRaises(AttributeError):
            p.__x
        with self.assertRaises(AttributeError):
            p.x = 1
        
        # y 
        with self.assertRaises(AttributeError):
            p.__y
        with self.assertRaises(AttributeError):
            p.y = 1


    def test_3_get_coords(self):
        p = P(1,2)
        self.assertEqual(p.get_coords(), (1,2))
    
    def test_4_equal(self):
        p1 = P(0,0)
        self.assertTrue(P.equal(p1, P(0.,0)))
        self.assertFalse(P.equal(p1, P(1, 0)))
    
    
if __name__ == '__main__':
    unittest.main()