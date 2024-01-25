#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(self,size=0,position=(0,0)):
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
    def size(self,value):
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
        """Retrieves the position of the square
        Returns:
            int: The current position of the square
        """
    @position.setter
    def position(self,value):
        """Sets the position of the square
        Raises:
            TypeError: if the position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple)or len(value) != 2 or not all(isinstance(num,int)for num in value)or not all(num >= 0 in value for num in value)):
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value
    def area(self):
        """Return the current area of the square"""
        return(self.__size*self.__size)
    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print("")
            return
        print(" " * self.__position[1], end= "")
        for i in range(0,self.__size):
            print(" " * self.__position[0], end= "")
            print("#" * self.__size, end= "")
