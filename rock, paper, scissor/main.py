# Rock, Paper, Scissors Game (User vs Computer)
# --------------------------------------------
# The user plays against the computer.
# Computer randomly chooses rock, paper, or scissors.
# The winner is decided based on the classic rules.

import random  # Import random module for computer's choice

def main():
    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    
    # List of possible moves
    options = ["rock", "paper", "scissors"]

    # Ask user for their choice
    user = input("Your move: ").lower()
    
    # Computer randomly selects a move
    computer = random.choice(options)

    # Show computer's move
    print(f"Computer chose: {computer}")

    # Check for tie
    if user == computer:
        print("It's a tie!")
    # Rock beats scissors
    elif user == "rock" and computer == "scissors":
        print("You win! Rock crushes scissors.")
    # Paper beats rock
    elif user == "paper" and computer == "rock":
        print("You win! Paper covers rock.")
    # Scissors beats paper
    elif user == "scissors" and computer == "paper":
        print("You win! Scissors cut paper.")
    # All other cases: user loses
    elif user in options:
        print("You lose!")
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")

# Run the game
if __name__ == "__main__":
    main()
