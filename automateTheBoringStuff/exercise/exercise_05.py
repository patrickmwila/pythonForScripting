#!/usr/bin/python3
from sys import *

def spam(divide_by):
    return 42 / divide_by

print('This programme output\'s result when 42 is divided by any integer.')
print('Simply type exit to exit the programme.')


while 'user_input_is_not_exit':
    response = input('\nEnter integer: ')
    if response != 'exit':
        try:
            response = int(response)

            try:
                division_result = spam(response)
            except ZeroDivisionError:
                print('Undefined! You can not divide any number by 0.')
                print('Try again')
                continue

            print(f'42 / {response} = {division_result}')

        except ValueError:
            print('Invalid Entry. Try again')
            continue

    elif response == 'exit':
        exit()

