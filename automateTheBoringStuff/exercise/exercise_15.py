#!/usr/bin/python3
#Dictionaries in python3

birthdays = {'Alice': 'Apr 1', 'Bod': 'Dec 12', 'Carol': 'Mar 4', 'Esther': 'Dec 22'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

