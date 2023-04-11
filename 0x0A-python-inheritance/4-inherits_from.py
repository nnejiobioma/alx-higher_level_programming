#!/usr/bin/python3

"""Task four. function that
checks and returns true if the object
is an instatnce of a class that inherites specified class
"""


def inherits_from(obj, a_class):
    """Returns true id the object of an instance is a
    class that inherited directly or indirectly the
    specifief class
    """
    if type(obj) and isinstance(obj, a_class) != a_class:
        return True
    else:
        return False
