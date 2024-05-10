#!/usr/bin/python3
"""Creates a copy of the string,
   remvong the character at n position.
   """

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
