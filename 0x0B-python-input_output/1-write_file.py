#!/usr/bin/python3
"""This module contains a function that writes a string
to a text file (UTF8) and returns the number
of characters written"""


def write_file(filename="", text=""):
    """
    Writes the given text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
