import unittest
from Boundary import Boundary

class Boundary_test(unittest.TestCase):

    def test_create_boundary(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        boundary = Boundary((x1, y1), (x2, y2))
        self.assertIsInstance(boundary, Boundary)
        self.assertEqual(boundary.p1, (x1, y1))
        self.assertEqual(boundary.p2, (x2, y2))

if __name__ == '__main__':
    unittest.main()