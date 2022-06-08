#!/usr/bin/python3
""" 12. Pascal's Triangle """


def pascal_triangle(n):
    """ function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    pascal = []
    prev = []

    for i in range(n):
        row = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                row.append(1)
            else:
                row.append(prev[p1] + prev[p2])
            p1 += 1
            p2 += 1
        pascal.append(row)
        prev = row[:]

    return pascal
