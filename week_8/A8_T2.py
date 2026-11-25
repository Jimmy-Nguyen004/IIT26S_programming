import A8_T2_lib as lib

def showOptions() -> None:
    print("Options:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n0 - Exit")
    return None

def ask_choice() -> int:
    choice = input("Your choice: ")
    try: choice = int(choice)
    except ValueError: # prevent wrong input from user
        choice = -1
    return int(choice)

def ask_value(PPrompt: str) -> float:
    value = float(input(PPrompt))
    return value

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = ask_choice()
        if choice == 1:
            value1 = ask_value("Insert first addend value: ")
            value2 = ask_value("Insert second addend value: ")
            print(f"{value1} + {value2} = {lib.add(value1, value2)}")
        elif choice == 2:
            value1 = ask_value("Insert minuend value: ")
            value2 = ask_value("Insert subtrahend value: ")
            print(f"{value1} - {value2} = {lib.subtract(value1, value2)}")
        elif choice == 3:
            value1 = ask_value("Insert multiplicand value: ")
            value2 = ask_value("Insert multiplier value: ")
            print(f"{value1} * {value2} = {lib.multiply(value1, value2)}")
        elif choice == 4:
            value1 = ask_choice("Insert dividend value: ")
            value2 = ask_choice("Insert divisor value: ")
            print(f"{value1} / {value2} = {lib.divide(value1, value2)}")
        elif choice == 0:
            print("Exiting program.")
            print()
            break
        else:
            print("Unknown option!")
        print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()