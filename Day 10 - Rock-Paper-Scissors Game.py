# Rock-Paper-Scissors – A simple game where the user plays against the computer.
import random

def computerChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
            (userChoice == 'scissors' and computerChoice == 'paper') or \
            (userChoice == 'paper' and computerChoice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


# Main game loop
def playGame():
    print("Welcome to Rock, Paper, Scissors!")

    userChoice = input("Enter rock, paper, or scissors: ").lower()

    if userChoice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose rock, paper, or scissors.")
        return

    computer_choice = computerChoice()
    print(f"Computer chose: {computer_choice}")

    result = winner(userChoice, computer_choice)
    print(result)

playGame()
