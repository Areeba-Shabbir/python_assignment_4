def main():
    #  adjective, noun, and verb
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")
    
    # Construct the fun sentence
    fun_sentence = f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!"
    
    # Print the result
    print(fun_sentence)

if __name__ == '__main__':
    main()