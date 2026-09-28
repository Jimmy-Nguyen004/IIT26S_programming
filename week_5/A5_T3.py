def askName():
    PName = input("Insert name: ")
    return PName

def greetUser(PName):
    print(f"Hello {PName}")
    return None

def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

main()