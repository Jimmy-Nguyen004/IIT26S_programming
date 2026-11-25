import A8_T4_lib as lib
import template as temp
from datetime import datetime

def show_choices() -> None:
    print("Options:\n1 - Calculate amount of timestamps during year\n2 - Calculate amount of timestamps during month\n3 - Calculate amount of timestamps during weekday\n0 - Exit")
    return None

def main() -> None:
    print("Program starting.")
    timestamps: list[datetime] = []
    filename = input("Insert filename: ")
    lib.read_timestamps(filename, timestamps)
    while True:
        show_choices()
        choice = temp.ask_choice()
        if choice == 1:
            year = int(input("Insert year: "))
            count = lib.calc_timestamps_in_years(year, timestamps)
            print("Amount of timestamps during year '{}' is {}".format(year, count))
        elif choice == 2:
            month = input("Insert month: ")
            count = lib.calc_timestamps_in_months(month, timestamps)
            print("Amount of timestamps during month '{}' is {}".format(month, count))
        elif choice == 3:
            weekday = input("Insert weekday: ")
            count = lib.calc_timestamps_in_weekdays(weekday, timestamps)
            print("Amount of timestamps during weekday '{}' is {}".format(weekday, count))
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