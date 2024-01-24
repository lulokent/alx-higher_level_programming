#!/usr/bin/python3
class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Intialize a new square.
        Args:
            size (int): The size of new square.Must be an integer and >= 0.
        """
        self.size = size
    @property
    def size(self):
        """Get/set the current size of the square.
        Returns: thie size of the the square.
        """
        return (self.__size)
    @size.setter
    def size(self,value):
        """Sets the current size of the square.
        size must be an integer.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the current area of the square."""
        return (self.__size*self.__size)
