lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cipher(text):
    result = ''
    for char in text:
        if char in lower:
            i = lower.find(char)
            i = i + 13
            if i >= 26:
                i = i - 26
            result = result + lower[i]
        elif char in upper:
            i = lower.find(char)
            i = i + 13
            if i >= 26:
                 i = i - 26
            result = result + upper[i]
        else:
            result = result + char

def main():
    print("Program starting.")
    print()
    print("Collecting plain text rows for ciphering.")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(cipher(row))
    print()

    print("1 - Show ciphered text")
    print("2 - Save ciphered text")
    choice = input("Your choice: ")
    print()

    if choice == "1":
        print("#### Ciphered text ####")
        for row in rows:
            print(row)
        print("#### Ciphered text ####")
    elif choice == "2":
        filename = input("Insert filename to save: ")
        if filename != "":
            file = open(filename, "w")
            for row in rows:
                file.write(row + "\n")
            file.close()
            print("Ciphered text saved!")
        else:
            print("File name not defined.")
            print("Aborting save operation.")
    else:
        print("Unknown option!")

    print("Program ending.")

main()