import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        # Test of Rectangle(1, 2) exists
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def testRect(self):
        # Test of Rectangle(1, 2, 3)
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def testRectXY(self):
        # Test of Rectangle(1, 2, 3, 4)
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertIsNotNone(rect.id)

    def widthIsNotInt(self):
        # Test of Rectangle("1", 2)
        # Raises TypeError
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        # Test of Rectangle(1, "2")
        # Raises TypeError
    def heightIsNotInt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        # Test of Rectangle(1, 2, "3")
        # Raises TypeError
    def xIsNotInt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        # Test of Rectangle(1, 2, 3, "4")
        # Raises TypeError
    def yIsNotInt(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        # Test of Rectangle(-1, 2)
        # Raises ValueError
    def widthIsNegative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        # Test of Rectangle(1, -2)
        # Raises ValueError
    def heightIsNegative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        # Test of Rectangle(0, 2)
        def widthIsZero(self):
            with self.assertRaises(ValueError):
                Rectangle(0, 2)

        # Test of Rectangle(1, 0)
        def heightIsZero(self):
            with self.assertRaises(ValueError):
                Rectangle(1, 0)

        # Test of Rectangle(1, 2, -3)
        def xIsNegative(self):
            with self.assertRaises(ValueError):
                Rectangle(1, 2, -3)

    def test_area(self):
        # Test when width = 5 and height = 10
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

        # Test when width = 3 and height = 7
        rect = Rectangle(3, 7)
        self.assertEqual(rect.area(), 21)

    def test_str(self):
        # Test when width = 5, height = 10, x = 2, y = 3, id = 1
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        # Test when updating with args: id = 1,
        # width = 5, height = 10, x = 2, y = 3
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(1, 5, 10, 2, 3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

        # Test when updating with kwargs: id = 2,
        # width = 7, height = 12, x = 4, y = 5
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(id=2, width=7, height=12, x=4, y=5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_to_dictionary(self):
        # Test when width = 5, height = 10, x = 2, y = 3, id = 1
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_output = {"x": 2, "y": 3, "id": 1, "height": 10, "width": 5}
        self.assertEqual(rect.to_dictionary(), expected_output)


if __name__ == '__main__':
    unittest.main()
