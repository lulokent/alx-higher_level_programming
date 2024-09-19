#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all element occurrences by another list."""
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
