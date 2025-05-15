MAX_LENGTH = 3  # Required max length of the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()       # Remove the last item
        print("Removed:", removed_item)  # Print removed item

def main():
    lst = []  # Initialize empty list

    while True:
        value = input("Enter a value (or press Enter to stop): ")
        if value == "":
            break
        lst.append(value)

    print("Original list:", lst)
    shorten(lst)
    print("Final list:", lst)

# This line runs the main function
if __name__ == '__main__':
    main()
