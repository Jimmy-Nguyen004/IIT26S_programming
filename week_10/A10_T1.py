########################################################
# Task A10_T1
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import numpy as np

def read_file(PFilename: str) -> np.ndarray:
    values: list[int] = []
    with open(PFilename, "r", encoding="UTF-8") as source:
        for line in source:
            line = line.strip()
            if len(line) == 0:
                continue
            values.append(int(line))
    return np.array(values)

def display_vertical(values: np.ndarray) -> None:
    print("# --- Vertically --- #")
    for value in values:
        print(value)
    print("# --- Vertically --- #")
    return None

def display_horizontal(values: np.ndarray) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(str(value) for value in values))
    print("# --- Horizontally --- #")
    return None

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = read_file(filename)
    display_vertical(values)
    display_horizontal(values)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()