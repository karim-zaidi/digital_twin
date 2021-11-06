import unittest

import numpy as np

from Area import Area
from AtomicZone import AtomicZone
from Point import P
from Wall import Wall


class AtomicZone_test(unittest.TestCase):
    
    def test_0_create_empty_atomiczone(self):
        self.assertIsInstance(AtomicZone(), AtomicZone)
    

    def test_1_create_atomiczone_from_area(self):
        # define area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, wall4])
        
        # define atomiczone
        atomiczone = AtomicZone(area=area)

        self.assertIsInstance(atomiczone, AtomicZone)
        self.assertEqual(atomiczone.areas, [area])


    def test_2_create_atomiczone_from_multiple_areas(self):
        # 1st area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area1 = Area('Kitchen', [wall1, wall2, wall3, wall4])
        
        # 2nd area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area2 = Area('Room', [wall1, wall2, wall3, wall4])

        # define atomiczone
        areas = [area1, area2]
        atomiczone = AtomicZone(area=areas)

        self.assertIsInstance(atomiczone, AtomicZone)
        self.assertEqual(atomiczone.areas, areas)


    def test_3_create_atomiczone_from_polygon(self):
        # define polygone
        polygon = [P(0,0),P(5,0),P(9,9),P(0,5)]

        # define atomiczone
        atomiczone = AtomicZone(polygon=polygon)

        self.assertIsInstance(atomiczone, AtomicZone)
        self.assertEqual(atomiczone.polygon, polygon)


    def test_4_add_single_area(self):
        # define atomiczone
        atomiczone = AtomicZone()
        
        # define area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area = Area('Kitchen', [wall1, wall2, wall3, wall4])

        # add area
        atomiczone.add_area(area)

        self.assertEqual(atomiczone.areas, [area])
    

    def test_5_add_multiple_areas_in_one_go(self):
        # define atomiczone
        atomiczone = AtomicZone()
        
        # 1st area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area1 = Area('Kitchen', [wall1, wall2, wall3, wall4])
        
        # 2nd area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area2 = Area('Room', [wall1, wall2, wall3, wall4])

        # add areas
        areas = [area1, area2]
        atomiczone.add_area(areas)

        self.assertEqual(atomiczone.areas, areas)


    def test_5_add_multiple_areas_one_at_a_time(self):
        # define atomiczone
        atomiczone = AtomicZone()
        
        # 1st area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area1 = Area('Kitchen', [wall1, wall2, wall3, wall4])
        
        # add area
        atomiczone.add_area(area1)

        # 2nd area
        wall1 = Wall(P(0, 0), P(10,0))
        wall2 = Wall(P(10, 0), P(10,10))
        wall3 = Wall(P(10,10), P(0,10))
        wall4 = Wall(P(0,10), P(0,0))
        area2 = Area('Room', [wall1, wall2, wall3, wall4])

        # add area
        atomiczone.add_area(area2)
        
        self.assertIsInstance(atomiczone, AtomicZone)
        self.assertEqual(atomiczone.areas, [area1, area2])


    def test_6_add_single_polygon(self):
        # TODO: uncomment
        # define atomiczone
        atomiczone = AtomicZone()
        
        # define polygon
        polygon = [P(0,0),P(5,0),P(9,9),P(0,5)]

        # add polygon
        # atomiczone.add_polygon(polygon)

        #self.assertEqual(atomiczone.polygon, [polygon])


    def test_7_add_multiple_polygon_in_one_go(self):
        # TODO: uncomment

        # define atomiczone
        atomiczone = AtomicZone()
        
        # define polygons
        polygon1 = [P(0,0),P(5,0),P(9,9),P(0,5)]
        polygon2 = [P(3,0),P(7,0),P(7,11),P(6,10),P(3,9)]

        polygons = [polygon1, polygon2]
        # add polygon
        # atomiczone.add_polygon(polygons)

        #self.assertEqual(atomiczone.polygon, polygons)


    def test_8_add_multiple_polygon_one_at_a_time(self):
        # TODO: uncomment

        # define atomiczone
        atomiczone = AtomicZone()
        
        # define polygon
        polygon1 = [P(0,0),P(5,0),P(9,9),P(0,5)]

        # add polygon
        # atomiczone.add_polygon(polygon1)
        
        # define polygon
        polygon2 = [P(3,0),P(7,0),P(7,11),P(6,10),P(3,9)]

        # add polygon
        # atomiczone.add_polygon(polygon2)

        #self.assertEqual(atomiczone.polygon, [polygon1, polygon2])


    def test_9_polygon_to_array(self):
        atomiczone = AtomicZone(polygon = [P(0,0),P(5,0),P(9,9),P(0,5)])
        coords = np.array([[0, 0], [5, 0], [9, 9], [0, 5]])
        self.assertTrue((atomiczone.polygon_to_array() == coords).all())


    def test_10_polygon_contain(self):
        atomiczone = AtomicZone(polygon = [P(0,0),P(5,0),P(9,9),P(0,5)])
        self.assertTrue(atomiczone.contains([0, 0, 0]))
        self.assertFalse(atomiczone.contains([0, 10, 10]))



if __name__ == '__main__':
    unittest.main()
