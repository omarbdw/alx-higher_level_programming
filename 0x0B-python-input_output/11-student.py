#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of student with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation of a
        Student instance"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation of a
        Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """Public method that replaces all attributes
        of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
