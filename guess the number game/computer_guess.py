# Guess the Number Game (Computer guesses the number)
# --------------------------------------------------
# In this game, the user thinks of a number between 1 and 100.
# The computer will try to guess it based on the user's feedback.

def main():
    print("Think of a number between 1 and 100.")
    input("Press Enter when you're ready...")  # Pauses until user is ready

    # Initialize the range in which the computer will guess
    low = 1          # Starting point of range
    high = 100       # Ending point of range
    feedback = ""    # Stores user feedback: 'h', 'l', or 'c'

    # Loop runs until the computer guesses correctly
    while feedback != "c":
        # Computer guesses the middle number of the current range
        guess = (low + high) // 2
        print(f"My guess is: {guess}")

        # Ask the user for feedback on the guess
        # 'h' means too high, 'l' means too low, 'c' means correct
        feedback = input("Is it too (h)igh, too (l)ow, or (c)orrect? ").lower()

        # Adjust the range based on feedback
        if feedback == "h":
            high = guess - 1  # Narrow the guessing range by reducing high limit
        elif feedback == "l":
            low = guess + 1   # Narrow the guessing range by increasing low limit

    # If the loop ends, it means the computer guessed correctly
    print(f"🎉 Yay! I guessed your number: {guess}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
