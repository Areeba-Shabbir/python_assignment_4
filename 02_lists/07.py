def main():
    values = []  # Create an empty list

    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break  # Exit the loop if input is empty
        values.append(user_input)  # Add input to list

    print("Here's the list:", values)

# This provided line is required at the end
if __name__ == '__main__':
    main()
