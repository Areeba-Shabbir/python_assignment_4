# This program prints 10 random numbers in the range 1 to 100 using the random module.

import random  # Importing the random module to generate random numbers

def main():
    for _ in range(10):  # Loop will run 10 times
        number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(number, end=" ")  # Print number on the same line with a space

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
