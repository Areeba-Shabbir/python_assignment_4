import math

def main():
    # Ask for the lengths of the two sides
    side_AB = float(input("Enter the length of AB: "))
    side_AC = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse using the Pythagorean theorem
    hypotenuse_BC = math.sqrt(side_AB**2 + side_AC**2)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {hypotenuse_BC}")

if __name__ == '__main__':
    main()