import unittest
from Element import Element

class Element_test(unittest.TestCase):

    def test_create_element(self):
        element = Element((0,0), (0,0))
        self.assertIsInstance(element, Element)

    def test_id(self):
        (x1, y1), (x2, y2) = (0, 0), (10,0)
        element1 = Element((x1, y1), (x2, y2))
        self.assertEqual(element1.id, 1)

        (x1, y1), (x2, y2) = (0, 0), (10,0)
        element2 = Element((x1, y1), (x2, y2))
        self.assertEqual(element2.id, 2)

if __name__ == '__main__':
    unittest.main()