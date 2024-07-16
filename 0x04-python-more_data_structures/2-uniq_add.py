#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list."""
    n_list = []
    sum = 0
    for i in my_list:
        if i not in n_list:
            sum += i
            n_list.append(i)
    return sum