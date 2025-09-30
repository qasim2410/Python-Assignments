import random

print("Welcome to the PyPassword Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input("How many passwords would you like to generate? "))
length = int(input("How many characters would you like your password to be? "))

length = input("Input the length of password: ")
length = int(length)

print("\nHere are your passwords:")

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)