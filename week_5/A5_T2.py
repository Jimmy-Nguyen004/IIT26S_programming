def frame_word(word):
    a = "*" * (len(word) + 4)
    print(a)
    print("* " + word + " *")
    print(a)
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frame_word(word)
    print()
    print("Program ending.")
    return None

main()
    