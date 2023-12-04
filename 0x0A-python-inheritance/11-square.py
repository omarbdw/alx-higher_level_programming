#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Instantiation with width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return string representation of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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

    def __str__(self):
        """ Return string representation of square """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def print(self):
        """ Print square description """
        print("[Square] {}/{}".format(self.__size, self.__size))
