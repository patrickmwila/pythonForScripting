#!/usr/bin/python3
#Exiting a program in python3
from sys import *


while True:
    response = input('Type exit to exit: ')
    if response == 'exit':
        exit()
    
    print(f'You typed: \'{response}\'.')
