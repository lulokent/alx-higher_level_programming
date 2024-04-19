#!usr/bin/python3
"""Defines a square-printing function."""

def print_square(size):
    """Print a square with a # character.

    Args:
        size (int): The height/width of the square.
    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than zero.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size is < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and is < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="")for j in range(size)]
        print("")
