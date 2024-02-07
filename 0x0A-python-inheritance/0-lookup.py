#!/usr/bin/python3

def lookup(obj):
    """Returns a list object's avaivable attributes.

    Args:
        obj: The input object to be processed.
    """
    return (dir(obj))
