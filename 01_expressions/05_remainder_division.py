def main():
    # Ask the user for the first number
    num1 = int(input("Please enter an integer to be divided: "))
    
    # Ask the user for the second number
    num2 = int(input("Please enter an integer to divide by: "))
    
    # Calculate the result of the division and the remainder
    result = num1 // num2
    remainder = num1 % num2
    
    # Print the result
    print(f"The result of this division is {result} with a remainder of {remainder}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()