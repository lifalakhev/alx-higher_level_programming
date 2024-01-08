#!/usr/bin/python3
"""Defines a class function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of or if the object is
    an instance of a class that inherited from the specified class.

    Args:
        obj (a_class): object to check type.
        a_class (type): type of type to check.

    Returns:
        boolean: True or False.
    """
    # print("---> obj type {}".format(type(obj)))
    # print("---> a_class type {}".format(type(a_class)))
    return isinstance(obj, a_class)
