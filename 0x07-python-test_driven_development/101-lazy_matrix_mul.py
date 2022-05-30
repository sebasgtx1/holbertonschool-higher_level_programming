#!/usr/bin/python3
""" Module that contains a function for multiplie 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Funtion that multiples two matrices
        Args:
            m_a (list of lists of ints or floats): matrix one
            m_b (list of lists of ints or floats): matrix two
        Return:
            the result matrix
    """
    return (np.dot(m_a, m_b))
