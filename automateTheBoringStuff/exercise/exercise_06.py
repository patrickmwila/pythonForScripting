#!/usr/bin/python3
#Guess game

from random import *
from sys import *

r = randint(1, 12)
guessesTaken = 1

def guessGame():
    global guessesTaken
    userName = input('Enter your name: ')
    print(f'Welcome {userName.title()}, this is guess my number game.')
    print('You have a total of three chances to guess my number.\n')

    while guessesTaken < 4:
        print('Iam thinking of a number between 1 and 12.')
        userGuess = input('Take a guess: \n')
        userGuess = int(userGuess)

        if userGuess > r:
            print('Your guess is too high.')
            guessesTaken += 1
            continue

        elif userGuess < r:
            print('Your guess is too low.')
            guessesTaken += 1
            continue

        elif userGuess == r:
            if guessesTaken == 1:
                print(f'Good job! You guessed my number in just {guessesTaken} guess trial.')
                print('you have earned a Gold STAR ****!')
                exit()
            else:
                print(f'Good job! You guessed my number in {guessesTaken} guesses. You can do better')
                exit()


    print(f'\nSorry, you\'re out of lives! my secrete number is: {r}.')


guessGame()
