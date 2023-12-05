#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ Instantiation of attributes for student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dictionary representation of student object """
        return self.__dict__

    def to_json(self, attrs=None):
        """ Returns dictionary representation of student object """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
