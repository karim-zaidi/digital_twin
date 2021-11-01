import unittest
from Element import Element


class Element_test(unittest.TestCase):

    def test_0_create_element(self):
        element = Element((0, 0), (0, 0))
        self.assertIsInstance(element, Element)

    def test_1_create_error(self):
        with self.assertRaises(AssertionError):
            Element([1, 0], [0, 0])

    def test_2_alignement_error(self):
        with self.assertRaises(AssertionError):
            Element((1, 1), (0, 0))

    def test_3_id_increment(self):
        (x1, y1), (x2, y2) = (0, 0), (10, 0)
        element1 = Element((x1, y1), (x2, y2))
        element2 = Element((x1, y1), (x2, y2))
        self.assertTrue(element1.id == 1 and element2.id == 2)

    def test_4_id_error(self):
        (x1, y1), (x2, y2) = (0, 0), (10, 0)
        element = Element((x1, y1), (x2, y2))
        with self.assertRaises(AttributeError):
            element.__id
        with self.assertRaises(AttributeError):
            element.id = 1

    def test_5_attribut(self):
        element = Element((0, 0), (10, 0))
        self.assertTrue(element.p1 == (0, 0) and element.p2 == (10, 0))

    def test_6_attribut_error(self):
        element = Element((0, 0), (0, 0))
        with self.assertRaises(AttributeError):
            element.__p1
            element.__p2

    def test_7_attribut_change(self):
        element = Element((0, 0), (10, 0))
        element.p1 = (10, 0)
        element.p2 = (50, 0)
        self.assertTrue(element.p1 == (10, 0) and element.p2 == (50, 0))

    def test_8_attribut_change_error(self):
        element = Element((0, 0), (10, 0))
        with self.assertRaises(AssertionError):
            element.p1 = (30, 30)

    def test_9_get_coord(self):
        element = Element((0, 0), (10, 0))
        self.assertTrue(element.get_x_coords() == (0, 10)
                        and element.get_y_coords() == (0, 0))


if __name__ == '__main__':
    unittest.main()
