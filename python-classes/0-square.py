#!/usr/bin/python3
"""
Square Module
This module defines a Square class.
"""
class Square:
    """
    Defines a square by its size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        Why 'size' is a private attribute?
        The size of a square is crucial for a square, many things depend on it
        (area computation, etc.), so the class builder must control the type
        and value of this attribute. One way to have this control is to keep
        it private. Future tasks will show how to get, update, and validate
        the size value.
        Args:
            size (int): The size of the new square.
        """
        # Private instance attribute __size is used to control access
        # Python's convention for private attributes is to prefix them with double underscores
        self.__size = size
