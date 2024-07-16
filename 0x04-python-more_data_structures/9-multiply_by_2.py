#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary wilth values multiplied by 2."""
    new_dict = a_dictionary.copy()

    for keys in list (new_dict.keys()):
        new_dict[keys] *= 2
    
    return (new_dict)
