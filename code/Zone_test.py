import unittest

from Zone import Zone


class Zone_test(unittest.TestCase):
    
    def test_0_create_empty_zone(self):
        zone = Zone()
        self.assertIsInstance(zone, Zone)
        self.assertTrue(zone.id == 0)
        self.assertFalse(zone.is_component)

if __name__ == '__main__':
    unittest.main()