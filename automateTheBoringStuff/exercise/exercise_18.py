#!/usr/bin/python3
"""
Nested Dictionaries and Lists
A program that uses a dictionary that contains other dictionaries
in order to see who is bringing what to a picnic.
"""
#Dictionary containing other dictionaries
all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}



def totalBrought(guests, key):
    """takes in a dictionary and value of inner dictionary
    in order to return the total num of each value in the inner dictionary
    """
    num_brought = 0

    for guest, dictionary in guests.items():
        num_brought = num_brought + dictionary.get(key, 0)
    return num_brought



print('Number of things being brought:')

for guest, dictionary in all_guests.items():                      # loop through all_guests
    for key, value in dictionary.items():                         # loop through the inner dictionary contained in all_guests
        totalBrought(all_guests, key)                             # invoke totalBrought(), passing it all_guests and the key generated from the inner loop line 28
        print(f'- {key.title()} {totalBrought(all_guests, key)}') # using formated string print the key in title case and invoke the totalBrought(), which should return the total number of how many times the key passed to it exists in the all_guests inner dictionary


