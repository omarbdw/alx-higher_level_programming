#!/usr/bin/python3
""" a function that prints a matrix of character # and size "size" """


def text_indentation(text):
    """
    Splits a given text into paragraphs based on \
        the occurrence of '.', '?', or ':' characters.

    Args:
        text (str): The text to be split into paragraphs.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = False
    for char in text:
        if flag is True and char == ' ':
            continue
        if char == '.' or char == '?' or char == ':':
            flag = True
            print(char)
            print()
        else:
            print(char, end="")
            flag = False
