# Countdown Timer in Python
# -------------------------
# The program counts down from a given number of seconds to zero.
# It updates the display every second until time runs out.

import time  # For delay functions

def countdown(seconds):
    # Loop from the given seconds down to 0
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1   # Decrease the seconds by 1
    
    print("Time's up! ⏰")

def main():
    print("Welcome to the Countdown Timer!")
    
    # Get user input for the number of seconds to count down
    total_seconds = int(input("Enter the countdown time in seconds: "))
    
    countdown(total_seconds)

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
