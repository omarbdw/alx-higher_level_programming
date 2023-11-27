#!/usr/bin/python3
class Rectangle:
    """This is a class defining a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Declares a rectangle.
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """Gets the width of the rectangle.
        """
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value < 0:
            raise ValueError(f"width must be >= 0")
        self.__width = value
