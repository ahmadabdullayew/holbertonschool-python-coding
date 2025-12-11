#!/usr/bin/python3
"""
0-square.py - Bu modül, Square sınıfını tanımlar.
Bu, ALX Python OOP görevlerinin 0. bölümü için zorunludur.
"""


class Square:
    """
    Bir kareyi, özel (private) bir 'size' niteliği ile tanımlayan sınıf.
    """


    def __init__(self, size):
        """
        Yeni bir Square örneğini başlatır.
        
        Args:
            size (int): Karenin boyutu (kenar uzunluğu).
        """
        self.__size = size
