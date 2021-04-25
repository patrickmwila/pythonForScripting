#!/usr/bin/python3
# write a program to find the sum of 1 + 2 + 3 + ... + nth_number

print("Enter a number, i'll output the sum from 1 + 2 + 3 + ... + nth_number.")
var_user_num = int(input())


def addition(int_value):
    var_sum = 0

    for i in range(1, int_value + 1):
        var_sum = var_sum + i


    return var_sum

print("The sum of numbers from 1 up to", var_user_num, "is", addition(var_user_num))


