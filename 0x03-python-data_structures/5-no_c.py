#!/usr/bin/python3

def no_c(my_string):
    """funtion that rwemoves all characters c and C."""

    str_copy = ""
    for element in my_string:
        if element != 'c' and element != 'C':
            str_copy += element
    return str_copy
