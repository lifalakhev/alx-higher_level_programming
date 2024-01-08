#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """Class that inherits from list."""
    def print_sorted(self):
        """prints a list in sorted order"""
        print(sorted(self))
