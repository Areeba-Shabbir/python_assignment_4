# Program to perform a countdown from 10 to 1, then print "Liftoff!"

def main():
    for i in range(10, 0, -1):  # Start at 10, stop before 0, step -1
        print(i, end=" ")       # Print on the same line with space
    print("Liftoff!")           # Print final message


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
