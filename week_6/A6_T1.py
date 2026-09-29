print("Program starting.")
print("This program can read a file.")

filename = input("Insert file name: ")

with open(f"week_6/files/{filename}", "r", encoding="utf-8") as file:
    content = file.read()

print(f'#### START "{filename}" ####')
print(content)
print(f'#### END "{filename}" ####')
print("Program ending.")