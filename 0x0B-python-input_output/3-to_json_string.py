#!/usr/bin/python3
"""Defines a function to_json_string"""
import json


def to_json_string(my_obj):
    """
    Returns:
        str: JSON representation of object.
    """
    # print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    # print("type my_obj--> {}".format(type(my_obj)))

    # serializing json
    return json.dumps(my_obj)
