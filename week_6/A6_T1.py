def read_file(filename) -> str:
    with open(f"week_6/files/{filename}", "r", encoding="utf-8") as file:
        content = file.read()
    return content

def main():
    print('Program starting.')
    print("This program can read a file.")
    filename = input("Insert filename: ")
    content = read_file(filename)
    print(f"### START \"{filename}\" ####")
    print(content)
    print(f'#### END "{filename}" ####')
    print('Program ending.')
    return None

main()