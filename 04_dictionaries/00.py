def main():
    # Dictionary to store counts of numbers
    number_counts = {}

    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        number = int(user_input)
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
