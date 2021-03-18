#!/usr/bin/python3

print("This application generates the HCF of 'n' numbers.")
userNums = int(input("How many numbers do you want to check for the HCF? "))

nums = []
nums_factors = []

while userNums != 0:
    for count in range(1, userNums + 1):
        n = int(input(f"Enter number{count}: "))
        nums.append(n)
    break


for i in range(0, len(nums)):
    for k in range(1, nums[i] + 1):
        if i / k == 0:
           nums_factors.append(k)
        


print(nums)
print(nums_factors)

