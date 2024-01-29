#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def guess_the_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Initialize variables
    attempts = 0
    max_attempts = 3

    print("Welcome to Guess the Number!")
    print("Try to guess the number between 1 and 10.")

    while attempts < max_attempts:
        # Get user input for the guess
        guess = int(input("Enter your guess: "))

        # Increment the attempts counter
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
guess_the_number()


# In[ ]:




