#!/usr/bin/python3
"""A module that defines a square."""
class Square:
    """Represents a square.
    This class defines a square by a private instance attribute 'size'.
    """
    def __init__(self, size):
        """Initializes a new instance of the Square class.
        Args:
            size: The size of the square. It has no type or value
                  verification as per the requirements.
        """
        self.__size = size
