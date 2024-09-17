#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a marrix of integers."""

    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if b != (len(matrix[a]) - 1):
                edge = ' '
            else:
                edge = ''
            print("{:d}".format(matrix[a][b]), end=edge)
        print()
