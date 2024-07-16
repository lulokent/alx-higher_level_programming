#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    dic_ord = list(a_dictionary.keys())
    dic_ord.sort()
    for v in dic_ord:
        print("{}: {}".format(v, a_dictionary.get(v))) 