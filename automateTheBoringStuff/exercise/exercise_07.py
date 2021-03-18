#!/usr/bin/python3
"""
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.

"""
from sys import *

while True:
    print('Enter Integer:')
    try:
        number = int(input())
        break
    except ValueError:
        print('Invalid number: Run the program again and enter an integer!')
        exit()


def collatz(number):
    if number % 2 == 0:
        even =  number // 2
        print(even)
        return even

    elif number % 2 == 1:
        odd =  3 * number + 1
        print(odd)
        return odd


while number != 1:
    number = collatz(number)

