#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
