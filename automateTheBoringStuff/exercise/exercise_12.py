#!/usr/bin/python3

def eggs(some_parameter):
    some_parameter.append('hello')


spam = [1, 2, 3, 4]
eggs(spam)

print(spam)
