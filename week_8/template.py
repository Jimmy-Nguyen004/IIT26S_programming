def ask_choice() -> int:
    choice = input("Your choice: ")
    try:
        availability = int(choice)
    except ValueError:
        return -1
    return availability