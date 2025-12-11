#!/usr/bin/python3
class Square:
    """ArithmeticError class that defines a square by size"""
    def __init__(self, size = 0):
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
if __name__ == "__main__":
    square = Square(5)
