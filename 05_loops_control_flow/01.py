# Program Description:
# This program prints all the terms in the Fibonacci sequence
# starting from 0 and continuing until the terms are less than 10,000.

def main():
    MAX_VALUE = 10000  # Constant: maximum value to stop printing
    a, b = 0, 1         # Starting values for Fibonacci sequence

    # Print Fibonacci numbers while they are less than MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b  # Generate the next term

# This provided line is required to run the main() function
if __name__ == '__main__':
    main()
