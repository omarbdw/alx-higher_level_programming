#!/usr/bin/python3
""" a function that prints a matrix of character # and size "size" """


def print_square(size):
    """Prints a square made of '#' characters.
    Args:
        size (int): The size of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
