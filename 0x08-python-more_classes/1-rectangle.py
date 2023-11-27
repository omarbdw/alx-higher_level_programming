#!/usr/bin/python3
"""This is a class defining a rectangle."""


class Rectangle:
    """This class is for the creation of a rectangle."""
    def __init__(self, width=0, height=0):
        """This function is the constructor.
        Attributes:
            attr1 (width)
            attr2 (height)
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """This function is a getter and return the value of the instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """This function is a setter and sets the value of the instance.
        Attributes:
            attr1 (value)
        """
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value < 0:
            raise ValueError(f"width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This function is a getter and return the value of the instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """This function is a setter and sets the value of the instance.
        Attributes:
            attr1 (value)
        """
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value < 0:
            raise ValueError(f"height must be >= 0")
        self.__height = value
