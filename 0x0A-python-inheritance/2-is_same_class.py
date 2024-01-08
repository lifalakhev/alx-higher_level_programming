#!/usr/bin/python3
"""Defines a class function is_same_class()."""


def is_same_class(obj, a_class):
    """
    Checkss if the object is exactly an instance of the
    specified class.

    Args:
        obj (a_class): object to check type.
        a_class (type): type of type to check.

    Returns:
        boolean: True or False
    """
    return type(obj) == a_class