#!/usr/bin/python3
"""Defines an integer addition function"""

def add_integer(a, b=98):
    """
    Adds two numbers.
    Float arguments are typecasted to integers before addition is performed.
    Raise:
        TypeError : If either a or b is not an integer and not a float.
    return:
     int: addition of a and b.
     """
     if ((not isinstance(a, int)and not isinstance(a, float))):
         raise TypeError("a must be an integer")
     if ((not isinstance(b,int)and not isinstance(b, float))):
        raise TypeError("b must be an integer")
     return (int(a) + int(b))
