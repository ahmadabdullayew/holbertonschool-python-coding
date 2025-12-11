#!/usr/bin/python3
"""
1-square module: Defines the Square class with private instance
attribute size and validates size for type (integer) and value (>= 0).
"""


class Square:
    """
    Defines a square by its size, with validation upon instantiation.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The length of the side of the square (default: 0).

        Raises:
            TypeError: If size is not an integer (size must be an integer).
            ValueError: If size is less than 0 (size must be >= 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
