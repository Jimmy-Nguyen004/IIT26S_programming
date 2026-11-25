########################################################
# Task A10_T2
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

def sum_of_values(values: np.ndarray) -> int:
    print("# --- Sum of numbers --- #")
    sum = 0
    for value in values:
        sum += int(value)
    print(sum)
    print("# --- Sum of numbers --- #")
    return sum

def product_of_values(values: np.ndarray) -> int:
    print("# --- Product of numbers --- #")
    prod = 1
    for value in values:
        prod *= int(value)
    print(prod)
    print("# --- Product of numbers --- #")
    return prod

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = read_file(filename)
    sum_of_values(values)
    product_of_values(values)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()