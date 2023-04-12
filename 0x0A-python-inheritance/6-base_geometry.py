#!/usr/bin/python3
"""
write an empty class BaseGeometry
"""


class BaseGeometry:
    """Class that is empty"""
    def area(self):
        """ Raises and exception with error
        method not called
        """
        raise Exception("area() is not implemented")
