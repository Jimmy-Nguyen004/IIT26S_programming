def readFile(filename: str):
    print(f"Reading file '{filename}' content.")
    content = ""
    with open(f"week_6/files/{filename}", "r", encoding="UTF-8") as source:
        content = source.read()
    print("File content ready in memory.")
    return content

def copyFile(filename: str, content: str):
    print(f"Writing content into file '{filename}'.")
    with open(filename, "w", encoding="UTF-8") as destination:
        destination.write(content)
    return None

def main():
    print("Program starting.")
    print("This program can copy a file.")
    source_file = input("Insert source filename: ")
    destination_file = input("Insert destination filename: ")
    content = readFile(source_file)
    copyFile(destination_file, content)
    print("Copying operation complete.")
    print("Program ending.")
    return None

main()