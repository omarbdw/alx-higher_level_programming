#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.
    Args:
        filename (str): The name of the file to be read.
    Returns:
        None
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
