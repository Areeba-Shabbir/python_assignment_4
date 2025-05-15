import random  # Import the random module to generate random numbers

def main():
    # Loop 10 times to generate 10 random numbers
    for _ in range(10):
        number = random.randint(1, 100)  # Generate a random number from 1 to 100 (inclusive)
        print(number, end=' ')  # Print the number on the same line with a space

    print()  # Move to a new line after printing all numbers

# This line calls the main function when the program is run
if __name__ == '__main__':
    main()
