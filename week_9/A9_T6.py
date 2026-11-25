########################################################
# Task A9_T6
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

def show_options() -> None:
    print("Options:\n1 - Insert line\n2 - Save lines\n0 - Exit")
    return None

def ask_choice() -> int:
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        return -1
    return choice

def insert_line(lines: list[str]) -> None:
    line = input("Insert text: ")
    lines.append(line + "\n")
    return None

def save_lines(lines: list[str]):
    filename = input("Insert filename: ")
    try:
        with open(filename, "w", encoding="UTF-8") as filehandle:
            for line in lines:
                filehandle.write(line + "\n")
    except OSError:
        print("Couldn't write file '{}'".format(filename))
    return None

def main():
    print("Program starting.")
    lines: list[str] = []
    try:
        while True:
            show_options()
            choice = ask_choice()
            if choice == 1:
                insert_line(lines)
                print()
            elif choice == 2:
                save_lines(lines)
                break
            elif choice == 0:
                break
            else:
                print("Unknown option!")
            print()
    except KeyboardInterrupt:
        while True: 
            if len(lines) == 0:
                print("Closing suddenly.")
            else:
                print("Keyboard interrupt and unsaved progress!")
                y_n = input("Save before quit (y/n)?: ")
                if y_n.lower() == "y":
                    save_lines(lines)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()