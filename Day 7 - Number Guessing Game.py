# Number Guessing Game – Let the user guess a random number between 1 and 10
import random # is important to generate random numbers
randomNumber = random.randint(1, 10)
userGuess = int(input("Enter your guess from 1 to 10: "))

if randomNumber == userGuess:
    print(f"Congratulations! You successfully guessed the number. It was {userGuess}.")
else:
    print(f"Try again, the number was {randomNumber}.")
