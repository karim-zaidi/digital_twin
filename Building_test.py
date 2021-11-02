import unittest

from Boundary import Boundary
from Building import Building
from Door import Door
from Floor import Floor
from Wall import Wall
from Window import Window


class Building_test(unittest.TestCase):

    def setUp(self):
        self.building = Building('Building')

    def test_0_create_empty_building(self):
        self.assertIsInstance(self.building, Building)

    def test_1_create_single_floor_building(self):
        self.building.create_floor(1)
        self.assertIsInstance(self.building.floors[1], Floor)

    def test_2_duplicate_floors(self):
        self.building.create_floor(1)
        with self.assertRaises(Exception):
            self.building.create_floor(1)

    def test_3_create_2_floors(self):
        self.building.create_floor(1)
        self.building.create_floor(2)
        self.assertTrue(self.building.floors[1].name == 1 and self.building.floors[2].name == 2)

    # TODO: Karim setUp teardown
    def test_4_add_wall(self):
        self.building.create_floor(1)
        self.building.add_wall(1, (0,0), (10,0))
        self.assertIsInstance(self.building.floors[1].dividers[0], Wall)

    def test_5_add_boundary(self):
        self.building.create_floor(1)
        self.building.add_boundary(1, (0,0), (10,0))
        self.assertIsInstance(self.building.floors[1].dividers[0], Boundary)

    def test_6_add_window(self):
        self.building.create_floor(1)
        self.building.add_wall(1, (0,0), (10,0))
        wall_id = self.building.floors[1].dividers[0].id
        self.building.add_window(1, wall_id, (0,0), (10,0))
        self.assertIsInstance(self.building.floors[1].dividers[0].windows[0], Window)

    def test_7_add_door(self):
        self.building.create_floor(1)
        self.building.add_wall(1, (0,0), (10,0))
        wall_id = self.building.floors[1].dividers[0].id
        self.building.add_door(1, wall_id, (0,0), (10,0))
        self.assertIsInstance(self.building.floors[1].dividers[0].doors[0], Door)

if __name__ == '__main__':
    unittest.main()
