def show_options():
    print("Options: ")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def ask_choice():
    choice = input("Your choice: ")
    return choice

def show(count):
    print(f"Current count - {count}")

def increase_count(count):
    count += 1
    return count


def main():
    print("Program starting.")
    count = 0

    while True:
        show_options()
        choice = ask_choice()
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            show(count)
        elif choice == "2":
            count = increase_count(count)
            print("Count increased!")
        elif choice == "3":
            count = 0
            print("Cleared count!")
        else:
            print("Unknown option!")
        print()
    print()
    print("Program ending.")
    
main()