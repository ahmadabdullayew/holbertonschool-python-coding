#!/usr/bin/python3
"""
Square module: Defines a Square class that manages its size
with validation and provides a method to compute its area.
"""


class Square:
    """
    Defines a square with size validation and area computation.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
