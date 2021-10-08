import unittest
from Zone import Zone

class Zone_test(unittest.TestCase):
    
    def create_empty_zone(self):
        zone = Zone()
        self.assertIsInstance(zone, Zone)

if __name__ == '__main__':
    unittest.main()