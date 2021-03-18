#!/usr/bin/python3
"""
What are dictionaries in python3
Distinguishing between Lists and Dictionary: Unlike lists, items in dictionaries are unordered.
Usefull Dictionary Methods: The keys(), values(), get(), default() and items() Methods
Checking Whether a Key or Value Exists in a Dictionary
pretty printing in dictionaries: using-- import pprint
pprint, pformat
"""
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}                       ## creates an empty dictionary 

for char in message:             ## loop through each char in message
    count.setdefault(char, 0)    ## update count_dict with a single char and associated value starting from 0
    count[char] += 1             ## increment the count_dict value by 1


pprint.pprint(count)
