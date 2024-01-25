#!/usr/bin/python3
"""Define a class of square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initializing a new Square.
        Args:
            size(int): The size of the new square.
        Raise:
            TypeError: If the size is not an integer
            ValueError: If the the size is less than 0.
        """
       if not isinstance(size, int):
           raise TypeError("size must be an integer")
       elif size < 0:
           raise ValueError("size must be >= 0")
       self.__size = size
