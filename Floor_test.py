import unittest
from Floor import Floor

class Floor_test(unittest.TestCase):
    
    def test_create_empty_floor(self):
        floor = Floor(1)
        self.assertIsInstance(floor, Floor)

if __name__ == '__main__':
    unittest.main()