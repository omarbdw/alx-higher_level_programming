import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        # Test constructor with default values
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

        # Test constructor with custom values
        square = Square(10, 2, 3, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_str(self):
        square = Square(5, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 5")

    def test_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update(self):
        square = Square(5, 1, 2, 3)
        square.update(4, 10, 5, 6)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 6)

        square.update(id=5, size=15, x=7, y=8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        square = Square(5, 1, 2, 3)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary, {"id": 3, "size": 5, "x": 1, "y": 2})


if __name__ == '__main__':
    unittest.main()
