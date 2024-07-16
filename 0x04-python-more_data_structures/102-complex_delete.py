#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    keys_list = list(a_dictionary.keys())

    for val_dict in keys_list:
        if value == a_dictionary.get(val_dict):
            del a_dictionary[val_dict]

    return (a_dictionary)