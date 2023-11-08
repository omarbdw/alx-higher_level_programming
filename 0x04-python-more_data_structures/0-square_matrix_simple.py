#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        newRow = []
        for element in row:
            newElement = element ** 2
            newRow.append(newElement)
        newMatrix.append(newRow)
    return (newMatrix)
