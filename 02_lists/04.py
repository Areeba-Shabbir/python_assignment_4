def add_three_copies(my_list, data):
    # Add 3 copies of data to the list (in-place)
    for _ in range(3):
        my_list.append(data)

def main():
    message = input("Enter a message to copy: ")

    data_list = []  # Empty list
    print("List before:", data_list)

    add_three_copies(data_list, message)

    print("List after:", data_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
