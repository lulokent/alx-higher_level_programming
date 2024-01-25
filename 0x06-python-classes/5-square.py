#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represents a square."""
    def __init__(self,size):
        """Initialize a new square.
        Args:
            size(int):The size of the new square.
        """
        self.size = size
    @property
    def size(self):
        """Retrieves the size of the square.
        Returns:
            int: The current size of the square.
        """
        return (self.size)
    @size.setter
    def size(self, value):
        """sets the size of the square.
        Raises:
            TypeError: if the size is not an integer.
            ValueError: If the size is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mucxt be >= 0")
        self.__size = value
    def area(self):
        """Calculate and returns the current area of the square.
        Returns:
            int: the area of square.
        """
        return (self.__size*self.__size)
    def my_print(self):
        """Prints the square # character."""
        for i in range(0, self.__size):
            [print("#", end="")for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

