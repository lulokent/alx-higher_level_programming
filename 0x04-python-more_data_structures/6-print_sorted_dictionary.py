#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints dictionary by order of keys."""
    dic_ord = list(a_dicitionary.keys())
    dic_ord.sort()
    for v in dic_ord:
        print("{}: {}".format(v, a_dictionary.get(v)))
