#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size(int):The size of the new square.
            position(int,int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.
        Returns:
            int: the current size of the square.
        """

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Raise:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        
        Args:
            value (tuple): The position to set.
        
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.
        
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return
        
        [print("") for _ in range(self.__position[1])]
        
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
