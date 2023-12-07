import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_with_id(self):
        rectangle = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(rectangle.id, 100)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)

    def test_init_without_id(self):
        rectangle = Rectangle(5, 10, 3, 4)
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_width_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("invalid", 10, 1, 2)

    def test_width_invalid_value(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 10, 1, 2)

    def test_height_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, "invalid", 1, 2)

    def test_height_invalid_value(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, -10, 1, 2)

    def test_x_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 10, "invalid", 2)

    def test_x_invalid_value(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, -1, 2)

    def test_y_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 10, 1, "invalid")

    def test_y_invalid_value(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, 1, -2)


if __name__ == '__main__':
    unittest.main()
