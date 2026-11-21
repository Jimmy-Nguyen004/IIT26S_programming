########################################################
# Task A9_T2
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

import sys

def readFile(PFilename: str) -> str:
    try:
        with open(PFilename, "r", encoding="UTF-8") as file:
            content = file.read()
            print(f"## {PFilename} ##")
            for row in content.splitlines():
                print(row.strip())
            print(f"## {PFilename} ##")
    except FileNotFoundError:
        print('Couldn\'t read file "{}".'.format(PFilename))
        sys.exit(0)

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    readFile(filename)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()