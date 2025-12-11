#!/usr/bin/python3
"""
Square module: Defines a Square class that manages its size
with validation and provides a method to compute its area.
"""
class Square:
    """
    Defines a square with a validated private size attribute.
    """
    def __init__(self, size=0):
        self.__size = size
    
    def get(self):
        """
        Getter for the size attribute.
        Returns:
            int: The size of the square.
        """
        return self.__size
    def set(self, value):
        """
        Setter for the size attribute with validation.
        Args:
            value (int): The size to set for the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """
        Computes the area of the square.
        Returns:
            float: The area of the square.
        """
        return self.__size ** 2
