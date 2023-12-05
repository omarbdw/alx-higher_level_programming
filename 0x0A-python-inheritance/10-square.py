#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle


""" class Square that inherits from Rectangle """""


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size):
        """ Instantiation with size """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return area of square """
        return self.__size ** 2
