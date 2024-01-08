#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """
    Defines a class MyInt and invert int operators (== and !=).

    Args:
        int (int): value
    """
    def __init__(self, value):
        """Creates new instances of class MyInt."""
        self.__value = value

    def __eq__(self, other):
        """
        Method equal.

        Args:
            other (int): integer.

        Returns:
            boolean: True or False.
        """
        return self.__value != other

    def __ne__(self, other):
        """
        Method not equal.

        Args:
            other (int): integer.

        Returns:
            boolean: True or False
        """
        return self.__value == other
