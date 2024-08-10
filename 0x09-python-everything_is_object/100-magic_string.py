#!/usr/bin/python3
def magic_string(static={"count": 0}):
    """Returns a string 'BestSchool' n times"""
    static["count"] += 1
    return str("BestSchool, " *static["count"])[:-2]