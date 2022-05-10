#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda rw: list(map(lambda elmt: elmt**2, rw)), matrix)))
