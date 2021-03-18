#!/usr/bin/python3

while True:
    name = input('What is your name? ')
    if name != 'patrick':
        continue
    
    password = input(f'Hello {name}. Enter your password (Hint: it is a fish): ')
    if password == 'swordfish':
        break
    

print('Acess Granted')
    

