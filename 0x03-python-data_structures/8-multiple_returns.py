#!/usr/bin/python3

def multiple_returns(sentence):
    """Function that returns the length of a string and its first character.
    """

    if not sentence:
        sentence = None
    if sentence:
        length = len(sentence)
    else:
        length = 0
    return (length, sentence if not sentence else sentence[:1])
