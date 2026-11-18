import time

def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    return None

def askChoice() -> str:
    choice = input("Your choice: ")
    return choice

def setPause() -> float:
    duration = float(input("Insert pause duration (s): "))
    return duration

def activatePause(PDuration: float) -> None:
    if PDuration <= 0:
        print("Pause is not set.")
        print("Set pause first.")
    else:
        print("Pausing for {} seconds.".format(PDuration))
        time.sleep(PDuration)
        print("Unpaused.")
    return None

def main() -> None:
    print("Program starting.")
    duration = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == "1":
            duration = setPause()
        elif choice == "2":
            activatePause(duration)
        elif choice == "0":
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