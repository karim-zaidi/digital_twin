import unittest

from Boundary import Boundary
from Floor import Floor
from Point import P
from Wall import Wall


class Floor_test(unittest.TestCase):
    def setUp(self):
        self.floor = Floor(1)

    def test_0_create_empty_floor(self):
        self.assertIsInstance(self.floor, Floor)

    def test_1_add_single_wall(self):
        wall = Wall(P(0,0), P(10,0))
        self.floor.add_divider(wall)

    def test_2_add_multiple_walls(self):
        wall1 = Wall(P(0,0), P(10,0)) 
        wall2 = Wall(P(10,0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        self.floor.add_divider([wall1, wall2, wall3, wall4])
    
    def test_3_add_single_boundary(self):
        boundary = Boundary(P(0,0), P(0,10))
        self.floor.add_divider(boundary)
    
    def test_4_add_multiple_boundaries(self):
        boundary1 = Boundary(P(0,0), P(10,0)) 
        boundary2 = Boundary(P(10,0), P(10,10))
        boundary3 = Boundary(P(10,10), P(0,10))
        boundary4 = Boundary(P(0,10), P(0,0))
        self.floor.add_divider([boundary1, boundary2, boundary3, boundary4])

    def test_5_add_walls_boundaries(self):
        wall1 = Wall(P(0,0), P(10,0)) 
        wall2 = Wall(P(10,0), P(10,10))
        boundary1 = Boundary(P(10,10), P(0,10))
        boundary2 = Boundary(P(0,10), P(0,0))
        self.floor.add_divider([wall1, boundary1, boundary2, wall2])
    
    def test_6_add_error(self):
        with self.assertRaises(AssertionError):
            self.floor.add_divider('wall')

    def test_7_get_divider_by_id(self):
        wall = Wall(P(0,0), P(10,0))
        self.floor.add_divider(wall)
        self.assertEqual(self.floor.get_divider_by_id(wall.id), wall)
    
    def test_8_get_divider_by_id_error(self):
        with self.assertRaises(ValueError):
            self.floor.get_divider_by_id(42)
    
    def test_9_remove_divider_by_id(self):
        wall = Wall(P(0,0), P(10,0))
        self.floor.add_divider(wall)
        self.floor.remove_divider_by_id(wall.id)
        self.assertEqual(self.floor.dividers, [])

    def test_10_remove_divider_by_id_error(self):
        with self.assertRaises(ValueError):
            self.floor.remove_divider_by_id(42)

if __name__ == '__main__':
    unittest.main()
