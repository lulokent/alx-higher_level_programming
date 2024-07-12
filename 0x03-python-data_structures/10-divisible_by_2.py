#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2 in a list."""
    list = []
    for element in my_list:
        if element % 2:
            list = list + [False]
        else:
            list = list + [True]
    return list
