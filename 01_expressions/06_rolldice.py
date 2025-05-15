
import random  # For simulating dice rolls

# Constant for number of sides on each die
NUM_SIDES = 6

def roll_two_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    return die1, die2, die1 + die2

def main():

    die1, die2, total = roll_two_dice()

    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()
