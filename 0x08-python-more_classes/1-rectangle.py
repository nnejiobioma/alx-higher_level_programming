#!/usr/bin/python3
"""
Empty class that defines a rectangle
"""


class Rectangle:
    """
    Empty representation of a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height
        by setting width and height of an object
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """gets the width of the Rectangle"""
            return self.__width

        @property
        def height(self):
            """gets the height of the Rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the height of the Rectangle"""
            if type(value) is not int:
                raise TypeError("height must be an interger")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        @width.setter
        def width(self, value):
            """sets the width of the Rectangle"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
