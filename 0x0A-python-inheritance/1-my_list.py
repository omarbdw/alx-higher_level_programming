#!/usr/bin/python3
"""This module contains a class MyList that inherits from list"""


class MyList(list):
    """This class inherits from list"""
    def __init__(self):
        """This method initializes an instance of the class"""
        super().__init__()

    def print_sorted(self):
        """This method prints the list, but sorted (ascending sort)"""
        print(sorted(self))
