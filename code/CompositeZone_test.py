import unittest

from Area import Area
from AtomicZone import AtomicZone
from CompositeZone import CompositeZone
from Point import P
from Wall import Wall


class CompositeZone_test(unittest.TestCase):

    def test_0_create_simple_compositezone(self):
        zone = AtomicZone()
        compositezone = CompositeZone(zone)

        self.assertIsInstance(compositezone, CompositeZone)
        self.assertEqual(compositezone.zones, [zone])


    def test_1_create_real_compositezone(self):
        # define zone
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, wall4])
        zone = AtomicZone(area=area)

        # create compositezone
        compositezone = CompositeZone(zone)
        self.assertEqual(compositezone.zones, [zone])


    def test_2_add_zone(self):
        # define compositezone
        zone_empty = AtomicZone()
        compositezone = CompositeZone(zone_empty)

        # define another zone
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, wall4])
        zone = AtomicZone(area=area)

        # add zone
        compositezone.add(zone)

        self.assertEqual(compositezone.zones, [zone_empty, zone])


    def test_3_remove_zone(self):
        # define compositezone
        zone_empty = AtomicZone()
        compositezone = CompositeZone(zone_empty)

        # remove zone
        compositezone.remove(zone_empty)

        self.assertEqual(compositezone.zones, [])


    def test_4_contain_method(self):
        # creating two distinct zone
        rectangle = AtomicZone(polygon = [P(10, 0), P(13,0), P(13,20), P(10, 20)])
        zone = AtomicZone(polygon = [P(0,0),P(5,0),P(9,9),P(0,5)])

        compositezone = CompositeZone([rectangle, zone])

        # testing points in the rectangle
        self.assertTrue(compositezone.contains([0, 10, 0]))
        self.assertTrue(compositezone.contains([0, 11.5, 10]))

        # testing points in zone
        self.assertTrue(compositezone.contains([0, 0, 0]))

        # testing point outside
        self.assertFalse(compositezone.contains([0, 20, 20]))


if __name__ == '__main__':
    unittest.main()
