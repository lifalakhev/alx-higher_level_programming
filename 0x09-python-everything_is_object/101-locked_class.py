#!/usr/bin/python3
"""
Defines a class LockedClass
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is named first_name.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """
        Creates new instances of LockedClass.
        """

        self.first_name = "first_name"
