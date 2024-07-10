 #!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that replace an element at a specific position."""
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    temp = list(my_list)
    temp[idx] = element
    return temp
