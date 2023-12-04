#!/usr/bin/python3
"""This module contains a function that returns True if the object is an
instance of, or if the object is an instance of a class that inherited from,
the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """This function returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class ;
    otherwise False.
    Args:
        obj: The object to inspect.
        a_class: The class to compare the object to.
    Returns:
        True if the object is an instance of, or if the object
        is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
