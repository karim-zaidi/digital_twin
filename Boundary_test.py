import unittest
from Boundary import Boundary
from Point import P

class Boundary_test(unittest.TestCase):

    def test_0_create_boundary(self):
        p1, p2 = P(0, 0), P(10,0)
        boundary = Boundary(p1, p2)
        self.assertIsInstance(boundary, Boundary)
        self.assertTrue(boundary.p1 == p1 and boundary.p2 == p2)

if __name__ == '__main__':
    unittest.main()