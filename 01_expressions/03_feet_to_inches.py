INCHES_IN_FOOT: int = 12

def main():
    # Take user input
    feet = float(input("Enter measurement in feet: "))
    
    # Calculate inches
    inches = INCHES_IN_FOOT * feet
    
    # Display result
    print(f"{feet} feet is equal to {inches} inches.")

# Program entry point
if __name__ == "__main__":
    main()
