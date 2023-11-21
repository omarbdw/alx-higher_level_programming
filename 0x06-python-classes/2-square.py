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
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
