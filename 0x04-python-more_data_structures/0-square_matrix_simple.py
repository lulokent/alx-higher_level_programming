#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    new_matrix = []
    for val in matrix:
        result = list(map(lambda x: x**2, val))
        new_matrix.append(result)
    return new_matrix
