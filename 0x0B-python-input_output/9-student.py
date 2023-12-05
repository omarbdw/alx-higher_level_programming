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
