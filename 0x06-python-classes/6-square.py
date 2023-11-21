#!/usr/bin/python3
"""Defines a class of Square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size.
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        Returns:
            None
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """
        Retrieves the position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, val):
        """
        Setter method for the position of the square.
        Args:
            val (tuple): The position of the square.
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if not (isinstance(val, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (val < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        elif not isinstance(val[0], int) or not isinstance(val[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = val

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        Setter method for the size of the square.
        Args:
            val (int): The size of the square.
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if not (isinstance(val, int)):
            raise TypeError("size must be an integer")
        elif (val < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
