# main.py
# Mad Libs Generator
# This program asks the user to input different types of words (like noun, verb, adjective)
# and fills them into a funny story template.

def main():
    # Asking the user for different types of words
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")
    animal = input("Enter an animal: ")

    # Story template with user inputs
    story = f"""
    Once upon a time in {place}, there was a very {adjective} {animal}.
    Every day, it would {verb} near the {noun}.
    The people in the town were always {emotion} to see it!
    And they all lived happily ever after.
    """

    # Printing the final story
    print("\n--- Your Mad Libs Story ---")
    print(story)

# Calling the main function
if __name__ == '__main__':
    main()
