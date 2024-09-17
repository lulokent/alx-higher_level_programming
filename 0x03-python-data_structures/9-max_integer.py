#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integerof a list."""

    if my_list:
        my_list.sort(reverse=True)
        return (my_list[0])
    return (None)
