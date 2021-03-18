#!/usr/bin/python3
#Understanding the 'in and not in' operators in python3
from sys import *

myPets = ['Zophie', 'Pooka', 'Fat-Tail']

while True:

    print('Enter a pet name or nothing to stop: ')
    name = input()

    if name == '':
        exit()

    elif name not in myPets:
        print(f'I do not have a pet named {name}')
    else:
        print(f'{name} is my pet.')

