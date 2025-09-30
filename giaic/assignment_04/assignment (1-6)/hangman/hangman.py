import random
from words import words
import string

# Function to get a valid word from the list
def get_valid_word(words):
    word = random.choice(words)  # Randomly chooses a word from the list
    while '-' in word or ' ' in word:  # Ensures the word does not contain '-' or ' '
        word = random.choice(words)
    return word  # Moved outside the loop to ensure correct function execution

# Hangman game function
def hangman():
    word = get_valid_word(words).upper()  # Convert word to uppercase
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters the user has guessed

    while len(word_letters) > 0:
        # Display letters used
        print('\nYou have used these letters:', ' '.join(used_letters))

        # Show the current state of the word (e.g., W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').upper()

        # Check if input is valid
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that letter. Try again.')

        else:
            print('Invalid character. Please try again.')

    print(f"\n🎉 Congratulations! You've guessed the word: {word} 🎉")

# Main function to handle game execution
def main():
    play_game = input("Do you want to play Hangman? (yes/no): ").strip().lower()
    if play_game == "yes":
        hangman()
    else:
        user_input = input('Type something: ')
        print(user_input)

# Ensures the script runs properly when executed
if __name__ == "__main__":
    main()
