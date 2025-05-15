def get_first_element(lst):
    # Print the first element of the list
    print("First element in the list is:", lst[0])

def main():
    # Ask how many elements to add
    num_elements = int(input("How many elements in your list? "))

    user_list = []
    for i in range(num_elements):
        item = input(f"Enter element #{i+1}: ")
        user_list.append(item)

    get_first_element(user_list)

# Required line to call the main function
if __name__ == '__main__':
    main()
