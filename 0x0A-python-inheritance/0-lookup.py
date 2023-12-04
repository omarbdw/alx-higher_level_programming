#!/usr/bin/python3
""" This module contains a function that returns the list of available"""


def lookup(obj):
    """
    This function takes an object as input and returns a list of all
    the attributes and methods of that object.
    Args:
        obj: The object to inspect.
    Returns:
        A list of strings representing the attributes
        and methods of the object.
    """
    return dir(obj)
