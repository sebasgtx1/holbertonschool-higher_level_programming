#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squere = matrix.copy()
    for i in range(len(matrix)):
        squere[i] = list(map(lambda x: x ** 2, matrix[i]))
    return squere
