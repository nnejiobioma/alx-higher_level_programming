#!/usr/bin/python3
"""
Module task 3 that returns a function
if the onject is an instance of an object.
"""


def is_kind_of_class(obj, a_class):
    """If the object is an instance, return
    True or False ; otherwise rtrun False
    """
    return isinstance(obj, a_class)
