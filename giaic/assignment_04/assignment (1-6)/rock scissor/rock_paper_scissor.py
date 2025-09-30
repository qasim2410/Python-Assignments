import random

def rock_paper_scissor():
    user = input("Enter your choice (rock, paper, scissor): ").lower()
    choices = ['rock', 'paper', 'scissor']
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!" 


def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissor') or (player == 'scissor' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

    # return False

print(rock_paper_scissor())
