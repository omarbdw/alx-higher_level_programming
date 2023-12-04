#!/usr/bin/python3
"""This module contains a function that
returns True if the object is exactly"""


def is_same_class(obj, a_class):
    """This function returns True if the object
    is exactly an instance of the
    specified class ; otherwise False.
    Args:
        obj: The object to inspect.
        a_class: The class to compare the object to.
    Returns:
        True if the object is exactly an instance of the specified class ;
        otherwise False.
    """
    return type(obj) == a_class
