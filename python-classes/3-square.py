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

    def size(self):
        """
        Computes the area of the square.
        Returns:
            float: The area of the square.
        """
        return self.__size
    @property
    def size(self):
        if not isinstance(self.size, (int, float)):
            raise TypeError("size must be a number")
        if self.size < 0:
            raise ValueError("size must be >= 0")

        self.__size = self.size
    
    def area(self):
        """
        Computes the area of the square.
        Returns:
            float: The area of the square.
        """
        return self.__size ** 2
