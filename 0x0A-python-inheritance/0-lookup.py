#!/usr/bin/python3
"""Return a function lookup()."""


def lookup(obj):
    """List of available attributes and methods.
    Args:
        obj (class): object
    """
    return dir(obj)
