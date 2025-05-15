def main():
    # Speed of light (m/s)
    C = 299_792_458

    # Input mass from user
    mass = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    energy = mass * (C ** 2)

    # Output results
    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"\n{energy} joules of energy!")

# Call main function
if __name__ == '__main__':
    main()
