#!/usr/bin/python3
"""Prints the number from 1 to 100 separated by space.
   for mutliplies of three print Fizz instead of a number,
   for mutliplies of five print Buzz instead of a number, and
   for mutliplies of both three and five print FizzBuzz.
   """

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end='')
        elif i % 5 == 0:
            print("Buzz", end='')
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end='')
        else:
            print("{:d}".format(i), end='')
        print(end=' ')
