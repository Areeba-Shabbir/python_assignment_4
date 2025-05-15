# Hangman Game in Python
# ---------------------
# The computer selects a secret word.
# The user guesses letters one by one.
# If the letter is in the word, it's revealed.
# If not, user loses a try.
# The user wins if they guess all letters before running out of tries.

import random  # For picking a random word

def main():
    print("Welcome to Hangman!")
    
    # List of words for the game
    word_list = ['python', 'computer', 'hangman', 'programming', 'challenge']
    
    # Computer selects a random word from the list
    secret_word = random.choice(word_list)
    
    guessed_letters = []  # To store letters guessed by the user
    tries = 6  # Number of allowed wrong guesses
    
    # Initialize the display word with underscores for each letter
    display_word = ['_'] * len(secret_word)
    
    # Game loop - runs until user wins or loses
    while tries > 0 and '_' in display_word:
        print("\nWord: ", ' '.join(display_word))
        print(f"Tries left: {tries}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()
        
        # Validate input - must be a single alphabet letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue
        
        # Add guess to guessed letters list
        guessed_letters.append(guess)
        
        # Check if guess is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Reveal the letter(s) in the display word
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1
    
    # After the loop ends, check if user won or lost
    if '_' not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame over! You ran out of tries.")
        print("The word was:", secret_word)

# Run the game only if this file is executed (not imported)
if __name__ == '__main__':
    main()
