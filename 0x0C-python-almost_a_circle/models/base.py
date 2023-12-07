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
    
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to file"""
        import json
        if list_objs is None:
            list_objs = []
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))
