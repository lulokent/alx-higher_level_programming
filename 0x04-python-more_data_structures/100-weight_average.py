#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of int tuples(<score>, <weight>)"""
    if not my_list:
        return 0
    
    nume = 0
    deni = 0

    for tupl in my_list:
        nume += tupl[0] * tupl[1]
        deni += tupl[1]
    return (nume/deni)