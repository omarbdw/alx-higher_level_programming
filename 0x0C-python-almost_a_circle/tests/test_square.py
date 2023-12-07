import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init_with_id(self):
        square = Square(5, 1, 2, 100)
        self.assertEqual(square.id, 100)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_init_without_id(self):
        square = Square(10, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_size_invalid_type(self):
        with self.assertRaises(TypeError):
            square = Square("invalid", 1, 2)

    def test_size_invalid_value(self):
        with self.assertRaises(ValueError):
            square = Square(-5, 1, 2)

    def test_x_invalid_type(self):
        with self.assertRaises(TypeError):
            square = Square(5, "invalid", 2)

    def test_x_invalid_value(self):
        with self.assertRaises(ValueError):
            square = Square(5, -1, 2)

    def test_y_invalid_type(self):
        with self.assertRaises(TypeError):
            square = Square(5, 1, "invalid")

    def test_y_invalid_value(self):
        with self.assertRaises(ValueError):
            square = Square(5, 1, -2)

    def test_str_representation(self):
        square = Square(5, 1, 2, 100)
        self.assertEqual(str(square), "[Square] (100) 1/2 - 5")

    def test_size_getter(self):
        square = Square(5, 1, 2, 100)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        square = Square(5, 1, 2, 100)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update_with_args(self):
        square = Square(5, 1, 2, 100)
        square.update(200, 10, 3, 4)
        self.assertEqual(square.id, 200)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_with_kwargs(self):
        square = Square(5, 1, 2, 100)
        square.update(id=200, size=10, x=3, y=4)
        self.assertEqual(square.id, 200)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        square = Square(5, 1, 2, 100)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary, {"id": 100, "size": 5, "x": 1, "y": 2})


if __name__ == '__main__':
    unittest.main()