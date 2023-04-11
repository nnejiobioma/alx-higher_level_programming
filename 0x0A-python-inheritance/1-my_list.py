#!/usr/bin/python3
"""Class that inherits from a list"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Prints the list in sorted form"""
        print(sorted(self))
