import A8_T3_lib as lib
import template as template

def show_choices() -> None:
    print("Options:\n1 - Read values\n2 - Amount of values\n3 - Calculate sum of values\n4 - Calculate average of values\n0 - Exit")
    return None

def read_values(PValues: list[float]) -> None:
    filename = input("Insert filename: ")
    PValues.clear()
    with open(filename, "r", encoding="UTF-8") as source:
        for row in source:
            row = row.strip()
            if row == "":
                continue
            PValues.append(float(row))
    return None

def main() -> None:
    print("Program starting.")
    values: list[float] = []
    while True:
        show_choices()
        choice = template.ask_choice()
        if choice == 1:
            read_values(values)
        elif choice == 2:
            print("Amount of values {}".format(len(values)))
        elif choice == 3:
            print("Sum of values {}".format(lib.calc_sum(values)))
        elif choice == 4:
            print("Average of values {}".format(lib.calc_average(values)))
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