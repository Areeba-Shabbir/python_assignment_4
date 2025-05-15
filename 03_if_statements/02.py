def main():
      # Ask the user to enter their age and convert it to an integer
    age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo (voting age is 16)
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    # Check if the user can vote in Stanlau (voting age is 25)
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    # Check if the user can vote in Mayengua (voting age is 48)
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")


# This line ensures that the main function runs when the program is executed
if __name__ == '__main__':
    main()
