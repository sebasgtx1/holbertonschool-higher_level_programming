#!/usr/bin/python3
""" 1. Divide a matrix:
    Write a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Funtion that devides a matrix by an number
        Args:
            matrix (list(list)): matrix of integers/floats
            div (int or float): divisor
        Return:
            a new matrix with the result
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    i = 0
    j = 0
    result = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        if not all([isinstance(item, list) for item in matrix]):
            raise TypeError(error)
        if len(matrix) == 0:
            raise TypeError(error)
        if not all([len(item) == len(matrix[0]) for item in matrix]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix)):
            if not all([isinstance(item, (int, float)) for item in matrix[i]]):
                raise TypeError(error)
            else:
                row = [round(element / div, 2) for element in matrix[i]]
                result.append(row)
    return result
