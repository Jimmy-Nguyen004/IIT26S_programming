def writeFile(first_name: str, last_name: str, filename: str):
    with open(f"week_6/{filename}", "w", encoding="utf-8") as file:
        file.write(first_name + "\n")
        file.write(last_name + "\n")

def main():
    print('Program starting.')
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    filename = input("Insert filename: ")
    writeFile(first_name, last_name, filename)
    print('Program ending.')
    return None
main()