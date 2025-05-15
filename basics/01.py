# This program asks the user for a number and keeps doubling it until it reaches or goes above 100

def main():
    # Ask the user to enter a number and convert it to integer
    curr_value = int(input("Enter a number: "))

    # Keep doubling the number and print each result until it becomes 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2  # double the value
        print(curr_value)  # print the new value

# Call the main function
if __name__ == '__main__':
    main()
