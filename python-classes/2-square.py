#!/usr/bin/python3
"""
2-square module: Defines the Square class with a private instance
attribute size, validates size, and calculates its area.
"""


class Square:
    """
    A class that defines a square by its private instance attribute: size.
    It includes an area calculation method.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        
        Args:
            size (int/float): The length of the side of the square.
        
        Raises:
            TypeError: If size is not an int or float ("size must be a number").
            ValueError: If size is less than 0 ("size must be >= 0").
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """
        Calculates and returns the current area of the square.
        
        Returns:
            float: The area of the square (size * size).
        """
        return self.__size ** 2
