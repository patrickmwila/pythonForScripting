#!/usr/bin/python3

var_sum = 0
var_nums = []

for i in range(4, 17):
    var_sum = var_sum + i
    var_nums.append(var_sum)


print("Mean = ", var_sum / len(var_nums))

