def main():
    phonebook = {}

    while True:
        action = input("Enter 'add' to add a contact, 'lookup' to find a number, or press enter to quit: ").strip().lower()
        if action == "":
            break
        elif action == "add":
            name = input("Enter contact name: ").strip()
            number = input("Enter phone number: ").strip()
            phonebook[name] = number
            print(f"Added {name} with number {number}.")
        elif action == "lookup":
            name = input("Enter contact name to lookup: ").strip()
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}.")
            else:
                print(f"No contact found for {name}.")
        else:
            print("Invalid option. Please enter 'add', 'lookup', or press enter to quit.")

if __name__ == '__main__':
    main()
