def show_options():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")


def insert_word():
    word = input("Insert word: ")
    return word

def show_word(word):
    print(f'Current word - "{word}"')


def show_reversed(word):
    print(f'Word reversed - "{word[::-1]}"')


def main():
    print("Program starting.")
    Word = ""

    while True:
        show_options()
        choice = input("Your choice: ")

        if choice == "1":
            Word = insert_word()
        elif choice == "2":
            show_word(Word)
        elif choice == "3":
            show_reversed(Word)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option.")

    print()
    print("Program ending.")
    
main()
