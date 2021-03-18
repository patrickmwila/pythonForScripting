#!/usr/bin/python3
#A more efficient way of performing the same task in exercise_08.py

catNames = []

while True:
    print(f'Enter the name of cat {len(catNames) + 1} or enter nothing to stop:')
    name = input()

    if name == '':
        break
    else:
        catNames = catNames + [name]   # List concatenation

print('The cat names are: ')
for catName in catNames:
    print(f'  {catName}')


