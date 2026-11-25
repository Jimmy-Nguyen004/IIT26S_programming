########################################################
# Task A9_T7
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

import sys
import os

def show_help():
    print("Invalid amount of arguments.")
    print("[USAGE] python A9_T7.py src_file dst_file")
    return None

def copy_file(src_file: str, des_file: str):
    print('Copying file "{}" to "{}".'.format(src_file, des_file))
    proceed = True
    if os.path.exists(des_file):
        print('Destination file "{}" already exists.'.format(des_file))
        y_n = input("Do you want to overwrite it? (y/n): ")
        if str(y_n).lower() != "y":
            proceed = False
    if proceed:
        try:
            with open(src_file, "r", encoding="UTF-8") as source:
                content = source.read()
            with open(des_file, "w", encoding="UTF-8") as destination:
                destination.write(content)
        except OSError:
            print('Couldn\'t copy "{}" to "{}".'.format(src_file, des_file))
            print("Exiting program.")
            sys.exit(-1)
    return None

def main():
    print("Program starting.")
    if len(sys.argv) == 3:
        src_file = sys.argv[1]
        des_file = sys.argv[2]
        print('Source file "{}"'.format(src_file))
        print('Destination file "{}"'.format(des_file))
        copy_file(src_file, des_file)
    else:
        show_help()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()