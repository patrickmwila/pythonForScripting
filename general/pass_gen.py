#!/usr/bin/python
# password generator using python
import random

# get password length and number of paswords to be generated from the user
passwd_length = int(input("Enter the number of characters you want your password to be: "))
passwd_count = int(input(f"How many {passwd_length} charater passwords should i generate: "))

def passwordGenerator(passwd_count, passwd_length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!£$&()_-<>@~?,."
    passwords = []

    gen_passwd = "" # string variable to hold generated password

    for count in range(0, passwd_count): # loop untill the number of passwords to be generated is met
        for turn in range(0, passwd_length): # loop untill password length is met
            passwd_char = random.choice(chars) # get a random char from chars and store it in passwd_char
            gen_passwd = gen_passwd + passwd_char

        passwords.append(gen_passwd)
        gen_passwd = "" # clean gen_passwd

    return passwords

password_list = passwordGenerator(passwd_count, passwd_length)


def displayPasswords(password_list):
    for password in password_list:
        print(password)


displayPasswords(password_list)


