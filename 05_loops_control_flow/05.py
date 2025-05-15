# Program to repeatedly double a number entered by the user until it is 100 or greater.

def main():
    curr_value = int(input("Enter a number: "))  # Get initial number from user

    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value)            # Print the doubled value


if __name__ == '__main__':
    main()
