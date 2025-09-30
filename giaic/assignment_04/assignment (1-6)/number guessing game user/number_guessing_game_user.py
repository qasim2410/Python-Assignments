import random

def number_guessing_game_computer(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Congratulations! You have guessed the number {random_number} correctly!")
    print("Welcome to the Number Guessing Game!")

number_guessing_game_computer(10)