#!/usr/bin/python3
"""Defines a class of Square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size):
        """
        Initializes a Square object with a given size.
        Args:
            size (int): The size of the square.
        Returns:
            None
        """
        self.__size = size
