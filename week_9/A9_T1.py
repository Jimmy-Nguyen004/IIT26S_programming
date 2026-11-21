########################################################
# Task A9_T1
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

def checkUserInput(PNum: str):
    try:
        return float(PNum)
    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(PNum))
        return None
    

def main() -> None:
    print("Program starting.")
    total = 0.0
    while True:
        num = input("Insert a floating-point value (0 to stop): ")
        checked = checkUserInput(num)
        if len(num) == 0:
            break
        if checked is None:
            continue
        total += checked
    print()
    print("Final sum is {:.2f}".format(total))
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()