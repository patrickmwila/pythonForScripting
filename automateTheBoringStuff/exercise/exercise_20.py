#!/usr/bin/python3
"""
String manipulation...
The isX string methods are helpful when you need to validate user
input
"""


while True:
    age = input('Enter your age: ')

    if age.isdecimal():
        break
    else:
        print('Please enter a number for your age.')


while True:
    print('Enter a new password (letters and numbers only):')
    user_password = input()

    if user_password.isalnum():
        break
    else:
        print('Passwords can only have letters and numbers.')


