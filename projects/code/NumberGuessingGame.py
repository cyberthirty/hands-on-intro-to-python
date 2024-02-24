
import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess == number:
        print("Congratulations! You guessed it.")
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
