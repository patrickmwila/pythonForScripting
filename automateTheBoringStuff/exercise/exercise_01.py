#!/usr/bin/python3
#This program says hello and asks for my name

print('Hello World!')
print('What is your name?')
my_name = input()

print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))

print('What is your age?')
my_age = input()
print('You will be ' + str((int(my_age) + 1)) + ' in a year.')
