#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """
    Defines properties of rectangle by: (based on 0-rectangle.py).
    """

    def __init__(self, width=0, height=0):
        """
        initializes new instances of Rectangle.

        Args:
            width: width of rectangle. Defaults to 0.
            height: height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Property setter for height of recyangle.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
