#!/usr/bin/python3

spam = ['apples', 'bananas', 'tofu', 'cats']

def listToStr(anyList):
    anyList = str(anyList)
    print(anyList, sep=', ')
    print(type(anyList))


listToStr(spam)
##print(type(spam))

