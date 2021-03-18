#!/usr/bin/python3
import math

print("""\nThis application takes in a number and generates
factors of that number with the quivalent quotient obtained
when the number is divided by each factor. Example if you
want to generate factors of 10 enter 11""")

user_number = int(input("\nEnter your number: "))

while user_number - 1 != 0:
    factors = []  ## create an empty list that will store all the factors

    for number in range(1, user_number):
        if (user_number - 1) % number == 0:
            factors.append(number)

    if len(factors) == 1:
        print(f"{user_number-1} has only one possible factor which is: ", factors[0])

    else:
        print(f"The list below are all possible factors of {user_number - 1}: ")
        print(factors)

    perfect_squares = []
    user_number = user_number - 1

    for perfect_square in factors:
        if user_number % math.sqrt(perfect_square) == 0:
            perfect_squares.append(perfect_square)

    if len(perfect_squares) == 1:
        print(f"Considering the results above, {user_number} has only one perfect_square which is: ", perfect_squares[0])

    else:
        print(f"\nFrom the list above the following are detected as perfect_squares: ")
        print(perfect_squares)

    print(f"\nTherefore: ")

    for perfect_square in perfect_squares:
        for factor in factors:
            if perfect_square * factor == user_number:
                print(f"{perfect_square} * {factor} = ", factor * perfect_square)


    break


if user_number - 1 == 0:
    print(f"The radicand {user_number - 1} can be evaluated to 0")

