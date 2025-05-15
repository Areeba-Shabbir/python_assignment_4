def main():
    # Set the minimum required height
    MIN_HEIGHT = 50

    # Ask the user how tall they are
    height_input = input("How tall are you? ")

    # Check if the user entered something
    if height_input:  # If the input is not empty
        height = int(height_input)  # Convert the input to an integer

        # Check if the height meets or exceeds the minimum
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
    else:
        # If no input was entered
        print("No height entered. Program ended.")

# This provided line is required to run the main() function
if __name__ == '__main__':
    main()
