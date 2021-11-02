import unittest
from Floor import Floor
from Wall import Wall
from Boundary import Boundary

class Floor_test(unittest.TestCase):
    def setUp(self):
        self.floor = Floor(1)

    def test_0_create_empty_floor(self):
        self.assertIsInstance(self.floor, Floor)
    
    def test_1_change_name(self):
        self.floor.name = 2
        self.assertTrue(self.floor.name == 2)

    def test_2_add_single_wall(self):
        wall = Wall((0,0), (10,0))
        self.floor.add_divider(wall)

    def test_3_add_multiple_walls(self):
        wall1 = Wall((0,0), (10,0)) 
        wall2 = Wall((10,0), (10,10))
        wall3 = Wall((10,10), (0,10))
        wall4 = Wall((0,10), (0,0))
        self.floor.add_divider([wall1, wall2, wall3, wall4])
    
    def test_4_add_single_boundary(self):
        boundary = Boundary((0,0), (0,10))
        self.floor.add_divider(boundary)
    
    def test_5_add_multiple_boundaries(self):
        boundary1 = Boundary((0,0), (10,0)) 
        boundary2 = Boundary((10,0), (10,10))
        boundary3 = Boundary((10,10), (0,10))
        boundary4 = Boundary((0,10), (0,0))
        self.floor.add_divider([boundary1, boundary2, boundary3, boundary4])

    def test_6_add_walls_boundaries(self):
        wall1 = Wall((0,0), (10,0)) 
        wall2 = Wall((10,0), (10,10))
        boundary1 = Boundary((10,10), (0,10))
        boundary2 = Boundary((0,10), (0,0))
        self.floor.add_divider([wall1, boundary1, boundary2, wall2])
    
    def test_7_add_error(self):
        with self.assertRaises(AssertionError):
            self.floor.add_divider('wall')

    def test_8_get_divider_by_id(self):
        wall = Wall((0,0), (10,0))
        self.floor.add_divider(wall)
        self.assertEqual(self.floor.get_divider_by_id(wall.id), wall)
    
    def test_9_get_divider_by_id_error(self):
        with self.assertRaises(ValueError):
            self.floor.get_divider_by_id(42)

    #TODO: Do we test for each divider if they cross each other?

if __name__ == '__main__':
    unittest.main()