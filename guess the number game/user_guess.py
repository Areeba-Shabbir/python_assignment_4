# Guess the Number Game (User guesses the number)
# --------------------------------------------------
# In this game, the computer selects a random number.
# The user keeps guessing until they guess it correctly.
# After each guess, the computer gives feedback: too high, too low, or correct.

import random  # Importing random module to generate a random number

def main():
    print("Welcome to the Guess the Number Game!")

    # Computer selects a random number between 1 and 10 (inclusive)
    number = random.randint(1, 10)

    guess = 0  # Initialize user's guess with a default value

    # Loop runs until the user's guess is equal to the randomly selected number
    while guess != number:
        # Ask the user to input their guess and convert it to an integer
        guess = int(input("Guess a number between 1 and 10: "))

        # Give feedback based on user's guess
        if guess < number:
            print("Too low! Try again.")  # If guess is less than number
        elif guess > number:
            print("Too high! Try again.")  # If guess is greater than number

    # When the loop ends, it means the user guessed correctly
    print(f"🎉 Correct! The number was {number}.")

# This line ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
