#!/usr/bin/python3
import random

print('====== defining functions ======')
def hello():
    print('howdy!')
    print('howdy!!!')
    print('hello there.')


hello()
hello()
hello()

print('\n====== understanding functions with parameters ======')

def hi(name):
    print(f'Hello {name.title()}')


hi('patrick')
hi('mwila')

print('\n===== understanding functions with return statements =====')

# This game returns a fortune answer based on what the input number is given to the function
# Hint: You can generate random numbers and feed it to the function to get multiple returns
# Hint: You can create a while loop to determine how many times you want to see the output to the console


def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'

    elif answer_number == 2:
        return 'It is decidedly so'

    elif answer_number == 3:
        return 'Yes'

    elif answer_number == 4:
        return 'Reply hazy try again'

    elif answer_number == 5:
        return 'Ask again later'

    elif answer_number == 6:
        return 'Concetrate and ask again'

    elif answer_number == 7:
        return 'My reply is no'

    elif answer_number == 8:
        return 'Outlook not so good'

    elif answer_number == 9:
        return 'Very doubtful'


count = 1
while count < 10:
#    r = random.randint(1, 9)   # generate random numbers from 1 to 9 and store it in r
#    fortune = get_answer(r)    # pass the random number to the get_answer() and store the return statement in fortune
#    print(fortune)             # print what is stored in fortune
    # Functional programming approach
    print(get_answer(random.randint(1,9)))
    count += 1                             # increment count by 1




