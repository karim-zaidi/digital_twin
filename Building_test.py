import unittest
from Building import Building
from Floor import Floor

class Building_test(unittest.TestCase):

    def test_create_empty_building(self):
        building = Building('Empty Building')
        self.assertIsInstance(building, Building)

    def test_create_single_floor_building(self):
        building = Building('Single Floor Building')
        building.create_floor(1)
        self.assertIsInstance(building.floors[0], Floor)

    def test_duplicate_floors(self):
        building = Building('Building')
        building.create_floor(1)
        with self.assertRaises(Exception):
            building.create_floor(1)

    def test_create_2_floors(self):
        building = Building('Building')
        building.create_floor(1)
        building.create_floor(2)
        self.assertTrue(building.floors[0].name == 1 and building.floors[1].name == 2)

if __name__ == '__main__':
    unittest.main()