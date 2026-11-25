def ask_name():
    PName = input("Insert name: ")
    return PName

def greet_user(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    name = ask_name()
    greet_user(name)
    print("Program ending.")
    return None

main()