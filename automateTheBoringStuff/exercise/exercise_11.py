#!/usr/bin/python3

print('Welcome to fortune teller!')
messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concetrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]


while True:
    print(f'Enter a number between 0 and {len(messages)}: ')
    print('Or enter nothing to stop.\n')
    user_num = input()

    if user_num == '':
        break
    else:
        user_num = int(user_num)
        print(messages[user_num])
        continue


print('\nSee you next time!')
