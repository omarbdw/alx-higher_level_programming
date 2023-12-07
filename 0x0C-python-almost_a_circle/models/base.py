#!/usr/bin/python3
"""Base module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Returns JSON representation of list_dictionaries"""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)


@classmethod
def save_to_file(cls, list_objs):
    """Writes the JSON string representation of list_objs to a file"""
    filename = cls.__name__ + ".json"
    with open(filename, "w") as file:
        if list_objs is None:
            file.write("[]")
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            file.write(Base.to_json_string(list_dicts))


@staticmethod
def from_json_string(json_string):
    """Returns the list of the JSON string representation json_string"""
    import json
    if json_string is None or len(json_string) == 0:
        return []
    return json.loads(json_string)


@classmethod
def create(cls, **dictionary):
    """Returns an instance with all attributes already set"""
    if cls.__name__ == "Rectangle":
        dummy = cls(1, 1)
    elif cls.__name__ == "Square":
        dummy = cls(1)
    dummy.update(**dictionary)
    return dummy


@classmethod
def load_from_file(cls):
    """Returns a list of instances"""
    filename = cls.__name__ + ".json"
    try:
        with open(filename, "r") as file:
            list_dicts = Base.from_json_string(file.read())
            return [cls.create(**dictionary) for dictionary in list_dicts]
    except:
        return []
