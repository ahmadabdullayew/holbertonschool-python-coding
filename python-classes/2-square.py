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
        try:
            if not isinstance(size, (int, float)):
                raise TypeError("size must be a number")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except (TypeError, ValueError) as e:
            print(e)
            self.__size = 0
