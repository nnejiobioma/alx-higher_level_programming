#!/usr/bin/pythoy3
"""
Empty class that defines a rectangle
"""


class Rectangle:
	"""Empty representation of a rectangle"""
	def __init__(self, width=0, height=0):
		 """Initialize the Rectangle with a given width and height"""
		self.height = height
		self.width = width

	@property
	def width(self):
		"""getting the width of the Rectangle"""
		return self.__width

	@width.setter
	def width(self, value):
		"""updating the width of the Rectangle"""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""getting the height of the Rectangle"""
		return self.__height

	@height.setter
	def height(self, value):
		"""updating the height of the Rectangle"""
		if type(value) is not int:
		raise TypeError("height must be an integer")
	if value < 0:
		raise ValueError("height must be >= 0")
	self.__height = value
