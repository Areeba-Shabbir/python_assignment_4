def main():
    # Ask how many numbers to add
    count = int(input("How many numbers would you like to add? "))
    
    total = 0
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        total += num
    
    print(f"The total sum is: {total}")

# Call the main function
if __name__ == '__main__':
    main()
