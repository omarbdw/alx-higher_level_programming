#!/usr/bin/python3
"""
This module contains a function that
adds two integers or floats
and returns the sum.
"""
def add_integer(a, b=98):
    """ Adds two integers or floats and returns the sum.
    Args: a (int or float): The first number. b (int or float): The second number. Default is 98.
    Returns: int or float: The sum of a and b.isinstance """
    if not (a, (int, float)):
        raise TypeError(f"a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError(f"b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
