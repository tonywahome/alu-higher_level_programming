#!/usr/bin/python3
"""
class Square defined
"""

class Square:
    """
    This class represents Square
    """

    def __init__(self, size=0):
        """
        __init__ initializez Square class with a given size
        Arguments: size
        
        Raises: TypeError: If size is not an int
                ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size should be an int value")
        elif size < 0:
            raise ValueError("size should be greater than zero")
        else:
            self.__size = size
        
