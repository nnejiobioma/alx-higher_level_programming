#!/usr/bin/python3
"""
0-add_integer.py, This model adds two numbers
The numbers must be integers.
If the numbers are not integers it will return an error
"""
def add_integer(a, b=98):
    """
    Adds two integers
    
    Args:
    a: integer number
    b: integer number
    
    Returns:
    Addition of two integer numbers
    
    Raise:
    TyoeError when type a and b is not an integer
    
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a),
        b = int(b)
        return a+b
