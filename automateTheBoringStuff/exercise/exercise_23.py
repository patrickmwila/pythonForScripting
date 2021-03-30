#!/usr/bin/python3
print("This application generates the HCF of 'n' numbers.")
userNums = int(input("How many numbers do you want to check for the HCF? "))

nums = [] # list to store all numbers needed in the comparing of HCL
nums_factors = [] # list to store HCF

while 1:
    if userNums != 0: # loop until the userNums is met
        for count in range(1, userNums + 1): # generate a loop get userNums
            n = int(input(f"Enter number{count}: "))
            nums.append(n) # append the number
            
for i in range(0, len(nums)):
    for k in range(1, nums[i] + 1):
        if i / k == 0:
           nums_factors.append(k)
        


print(nums)
print(nums_factors)

