########################################################
# Task A9_T2
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

import sys

def main() -> None:
    print("Program starting.")
    code = int(input("Insert exit code(0-255): "))
    if code == 0:
        print("Clean exit")
    else:
        print("Error code")
    sys.exit(code)
    return None

if __name__ == "__main__":
    main()