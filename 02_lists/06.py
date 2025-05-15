def get_last_element(lst):
    # Print the last element of the list
    print("Last element in the list is:", lst[-1])

def main():
    # Create an empty list
    lst = []

    # Ask how many items user wants to enter
    n = int(input("How many elements in the list? "))

    # Take input and add items to the list
    for i in range(n):
        item = input(f"Enter element #{i+1}: ")
        lst.append(item)

    # Call function to get last element
    get_last_element(lst)

# This provided line is required at the end
if __name__ == '__main__':
    main()
