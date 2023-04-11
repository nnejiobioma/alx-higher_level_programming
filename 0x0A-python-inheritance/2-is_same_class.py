#!/usr/bin/python3

"""
Function that returns true if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """checkd if the object of the instance i
    s true then returns true, else returns false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
