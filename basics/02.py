# This program counts down from 10 to 1 and then prints "Liftoff!"

def main():
    # Loop from 10 to 1 (backward)
    for i in range(10, 0, -1):  # Start from 10, go to 1 (step -1)
        print(i, end=' ')  # Print number in same line with space

    # After the loop ends, print Liftoff!
    print("Liftoff!")

# Call the main function
if __name__ == '__main__':
    main()
