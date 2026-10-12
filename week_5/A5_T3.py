def askName():
    PName = input("Insert name: ")
    return PName

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    Name = askName()
    greetUser(Name)
    print("Program ending.")
    return None

main()