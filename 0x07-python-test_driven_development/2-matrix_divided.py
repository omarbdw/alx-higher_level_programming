#!/usr/bin/python3
""" a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a given divisor.
    Args:
        matrix (list): A matrix represented as a list of lists.
        div (int or float): The divisor.
    Returns:
        list: A new matrix with the elements divided by the divisor.
    Raises:
        ZeroDivisionError: If the divisor is zero.
        TypeError: If the matrix is not a valid matrix \
            or contains non-numeric elements.
    """
    newMatrix = []
    if not isinstance(div, (int, float)):
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        newRow = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list \
                    of lists) of integers/floats")
            element = round((element / div), 2)
            newRow.append(element)
        newMatrix.append(newRow)
    return newMatrix
