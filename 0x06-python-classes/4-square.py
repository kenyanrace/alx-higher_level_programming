#!/usr/bin/python3
class Square:
    """Write a class Square that defines a square:"""
    def __init__(self, size=0):
        """Module __init__ for size square validition"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method area return the square Area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Method property of size and return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method size_setter attribute evaluate the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
