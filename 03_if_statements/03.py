def main():
    # Ask the user to enter a year and convert it to an integer
    year = int(input("Enter a year: "))

    # Check leap year conditions:
    # A year is a leap year if it's divisible by 4,
    # NOT divisible by 100 unless it's also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# This line makes sure the main function runs when you execute the script
if __name__ == '__main__':
    main()
