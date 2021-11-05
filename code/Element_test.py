import unittest
from Element import Element
from Point import P


class Element_test(unittest.TestCase):

    def test_0_create_element(self):
        element = Element(P(0, 0), P(0, 0))
        self.assertIsInstance(element, Element)

    def test_1_create_element_error(self):
        with self.assertRaises(AssertionError):
            Element('1, 0', P(0, 0))
        with self.assertRaises(AssertionError):
            Element(P(1, 0), {0, 0})
        with self.assertRaises(AssertionError):
            Element(P(0, 0), (0, 0))
        with self.assertRaises(AssertionError):
            Element(P(0, 0), [0, 0])


    def test_2_alignement_error(self):
        with self.assertRaises(AssertionError):
            Element(P(1, 1), P(0, 0))

    def test_3_id_increment(self):
        (x1, y1), (x2, y2) = (0, 0), (10, 0)
        element1 = Element(P(x1, y1), P(x2, y2))
        element2 = Element(P(x1, y1), P(x2, y2))
        self.assertTrue(element1.id == 3 and element2.id == 4)

    def test_4_id_error(self):
        (x1, y1), (x2, y2) = (0, 0), (10, 0)
        element = Element(P(x1, y1), P(x2, y2))
        with self.assertRaises(AttributeError):
            element.__id
        with self.assertRaises(AttributeError):
            element.id = 1

    def test_5_attribut(self):
        element = Element(P(0, 0), P(10, 0))
        self.assertTrue(element.p1.x == 0 and element.p1.y == 0)
        self.assertTrue(element.p2.x == 10 and element.p2.y == 0)

    def test_6_attribut_error(self):
        element = Element(P(0, 0), P(0, 0))
        with self.assertRaises(AttributeError):
            element.__p1
        with self.assertRaises(AttributeError):
            element.__p2

    def test_7_attribut_change(self):
        element = Element(P(0, 0), P(10, 0))
        element.p1 = P(10, 0)
        element.p2 = P(50, 0)
        self.assertTrue(P.equal(element.p1, P(10,0)) and P.equal(element.p2, P(50,0)))

    def test_8_attribut_change_error(self):
        element = Element(P(0, 0), P(10, 0))
        with self.assertRaises(AssertionError):
            element.p1 = P(30, 30)

    def test_9_get_coord(self):
        element = Element(P(0, 0), P(10, 0))
        self.assertTrue(element.get_x_coords() == (0, 10) and element.get_y_coords() == (0, 0))

    def test_10_coincide(self):
        element1 = Element(P(0, 0), P(10, 0))
        element2 = Element(P(10, 0), P(0, 0))
        self.assertTrue(Element.coincide(element1, element2))

if __name__ == '__main__':
    unittest.main()
