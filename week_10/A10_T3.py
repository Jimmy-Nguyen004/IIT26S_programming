import sys

def readValues(PFilename: str, values: list[int]) -> None:
    values.clear()
    try:
        with open(PFilename, "r", encoding="UTF-8") as source:
            for line in source:
                value = line.strip()
                if len(value) == 0:
                    continue
                values.append(int(value))
    except (OSError, ValueError):
        print("Couldn't read file {}".format(PFilename))
        sys.exit(1)
    return None

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if PAsc and PValues[j] > PValues[j+1]:
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]
                swapped = True
            elif not PAsc and PValues[j+1] > PValues[j]:
                PValues[j+1], PValues[j] = PValues[j], PValues[j+1]
                swapped = True
        if not swapped:
            break
    return None

def displayValues(values: list[int]) -> None:
    print(", ".join(str(value) for value in values))
    return None

def main() -> None:
    values: list[int] = []
    print("Program starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print("The filename '{}' was passed via CLI.".format(filename))
    else:
        filename = input("Insert filename: ")
    readValues(filename, values)
    print("Raw '{}' -> ".format(filename), end="")
    displayValues(values)
    bubbleSort(values, PAsc=True)
    print("Ascending '{}' -> ".format(filename), end="")
    displayValues(values)
    bubbleSort(values, PAsc=False)
    print("Descending '{}' -> ".format(filename), end="")
    displayValues(values)
    values.clear()
    return None

if __name__ == "__main__":
    main()