# Program Description:
# This is a "Guess My Number" game.
# The program randomly picks a number between 0 and 99.
# The user tries to guess the number, and the program tells them if their guess is too high, too low, or correct.

import random

def main():
    secret_number = random.randint(0, 99)  # Random number between 0 and 99

    guess = int(input("I am thinking of a number between 0 and 99...\nEnter a guess: "))

    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        guess = int(input("Enter a new number: "))
    
    print(f"Congrats! The number was: {secret_number}")

# Required to run main function
if __name__ == '__main__':
    main()
