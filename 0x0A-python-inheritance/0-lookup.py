#!/usr/bin/python3

"""
This is a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Returns a list of object"""
    return dir(obj)
