# This program is a number guessing game where the user tries to guess a secret number between 0 and 99.

import random  # Import random module to generate a random number

def main():
    secret_number = random.randint(0, 99)  # Generate random number between 0 and 99
    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        guess = int(input("Enter a new number: "))

    # If guess is correct
    print(f"Congrats! The number was: {secret_number}")

# Required to call main function when script is run
if __name__ == '__main__':
    main()
