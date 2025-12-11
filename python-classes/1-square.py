#!/usr/bin/python3
"""
1-square module: Defines the Square class, which manages the size
of a square, enforces type and value validation, and can calculate its area.
"""


class Square:
    """
    A class that defines a square by its private instance attribute: size.
    It uses getter and setter properties for validation control.
    """


    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        
        Args:
            size (int/float): The length of the side of the square (default: 0).
        """
        # Call the setter to validate the initial size value
        self.size = size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current area of the square."""
        return self.__size ** 2
