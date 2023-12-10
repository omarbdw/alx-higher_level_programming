import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        # Test when list_dictionaries is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when list_dictionaries has one dictionary
        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expected_output = '[{"id": 1, "name"\
: "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_output)

    def test_from_json_string(self):
        # Test when json_string is empty
        self.assertEqual(Base.from_json_string(""), [])

        # Test when json_string has valid JSON
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expected_output = [{'id': 1, 'name': 'John'},
                           {'id': 2, 'name': 'Jane'}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_create(self):
        # Test when cls is Rectangle
        dictionary = {'id': 1, 'width': 10, 'height': 5}
        obj = Rectangle.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 5)

        # Test when cls is Square
        dictionary = {'id': 2, 'size': 7}
        obj = Square.create(**dictionary)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 7)

    def test_load_from_file(self):
        # Test when file does not exist
        self.assertEqual(Base.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
