#!/usr/bin/python3
"""This module contains a function that returns
True if the object is an instance of a class thatinherited
(directly or indirectly) from the
specified class; otherwise False."""


def inherits_from(obj, a_class):
    """ This function returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    Args:
        obj: The object to inspect.
        a_class: The class to compare the object to.
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ;
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
