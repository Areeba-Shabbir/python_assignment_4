def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 5.0,
        "durian": 30.0,
        "jackfruit": 15.5,
        "kiwi": 8.0,
        "rambutan": 11.0,
        "mango": 6.5
    }

    total = 0  # Initialize total cost

    # Loop through the dictionary and ask how many of each fruit the user wants
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total += quantity * price  # Calculate cost and add to total

    # Print the total cost
    print(f"\nYour total is ${total}")

if __name__ == '__main__':
    main()
