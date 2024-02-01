#!/usr/bin/python3

class Rectangle:
    """
    Class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional height and width.
        Args:
            width(int): The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

