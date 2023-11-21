#!/usr/bin/python3
"""Defines a class of Square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.
        Args:
            size (int): The size of the square.
        Returns:
            None
        """
        self.__size = size

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
        for i in range(self.__size):
            print(self.__size * '#')
