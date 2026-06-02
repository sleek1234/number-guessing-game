import random

number = random.randint(1, 10)
guess = None

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print("Correct! You guessed the number 🎉")