#!/usr/bin/python3
"""
Square class defined
"""


class Square:
    """
    this represnts the Square class
    """

    def __init__(self, size=0):
        """
        initializing square with given size
        Argument:
                 size(int)
        Raises:
               TypeError
               ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size should be an int")
        elif size < 0:
            raise ValueError("size should be greater than zero)"
        else:
            self.__size = size

    def area(self):
        """Calculates area of a square
           Returns integer 
        """
        return self.__size** 2
