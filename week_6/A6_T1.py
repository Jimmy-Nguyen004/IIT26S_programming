def readFile(filename) -> str:
    with open(f"week_6/files/{filename}", "r", encoding="utf-8") as file:
        Content = file.read()
    return Content

def main():
    print('Program starting.')
    print("This program can read a file.")
    filename = input("Insert filename: ")
    Content = readFile(filename)
    print(f"### START \"{filename}\" ####")
    print(Content)
    print(f'#### END "{filename}" ####')
    print('Program ending.')
    return None

main()