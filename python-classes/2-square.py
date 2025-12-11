#!/usr/bin/python3
class Square:
    """
    A class that defines a square by its size.
    """
    def __init__(self, size=0):
        try:    
            if not isinstance(size, (int, float)):
                raise TypeError("size must be a number")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except (TypeError, ValueError) as e:
            print(e)
            self.__size = 0
    def area(self):
        return self.__size ** 2
