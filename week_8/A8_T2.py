import A8_T2_addition as add
import A8_T2_subtraction as subt
import A8_T2_multiplification as multi
import A8_T2_division as divi

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None

def askChoice() -> int:
    choice = input("Your choice: ")
    try:
        choice = int(choice)
    except ValueError: # prevent wrong input from user
        choice = -1
    return int(choice)

def askValue(PPrompt: str) -> float:
    value = float(input(PPrompt))
    return value

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            value1 = askValue("Insert first addend value: ")
            value2 = askValue("Insert second addend value: ")
            print(f"{value1} + {value2} = {add.add(value1, value2)}")
        elif choice == 2:
            value1 = askValue("Insert minuend value: ")
            value2 = askValue("Insert subtrahend value: ")
            print(f"{value1} - {value2} = {subt.subtract(value1, value2)}")
        elif choice == 3:
            value1 = askValue("Insert multiplicand value: ")
            value2 = askValue("Insert multiplier value: ")
            print(f"{value1} * {value2} = {multi.multiply(value1, value2)}")
        elif choice == 4:
            value1 = askChoice("Insert dividend value: ")
            value2 = askChoice("Insert divisor value: ")
            print(f"{value1} / {value2} = {divi.divide(value1, value2)}")
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