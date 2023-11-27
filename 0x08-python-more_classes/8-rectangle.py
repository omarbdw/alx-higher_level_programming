#!/usr/bin/python3
"""This is a class defining a rectangle."""


class Rectangle:
    """This class is for the creation of a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This function is the constructor.
        Attributes:
            attr1 (width)
            attr2 (height)
        """
        self.height = height
        self.width = width
        self.number_of_instances += 1

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

    def area(self):
        """This function returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """This function returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """This function returns a string representation of the rectangle."""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """This function returns a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This function deletes an instance of Rectangle."""
        print("Bye rectangle...")
        self.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """This function returns the biggest rectangle based on the area.
        Attributes:
            attr1 (rect_1): The first rectangle.
            attr2 (rect_2): The second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError(f"rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError(f"rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
