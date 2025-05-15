# This program is a simple joke bot. It asks the user what they want.
# If the user types "Joke", it tells a specific joke.
# If the user types anything else, it says "Sorry I only tell jokes."

# Constants for prompt, joke, and sorry message
PROMPT = "What do you want? "
JOKE = ("Here is a joke for you!\n"
        "Panaversity GPT - Sophia is heading out to the grocery store.\n"
        "A programmer tells her: get a liter of milk, and if they have eggs, get 12.\n"
        "Sophia returns with 13 liters of milk.\n"
        "The programmer asks why and Sophia replies: 'because they had eggs'")
SORRY = "Sorry I only tell jokes"

def main():
    # Ask the user what they want
    user_input = input(PROMPT)
    
    # Check if the user wants a joke
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

# This provided line is required to call the main function
if __name__ == '__main__':
    main()
