print("Program starting.")
first_name = input("Insert first name: ")
last_name = input("Insert last name: ")
filename = input("Insert filename: ")

with open(filename, "w", encoding="utf-8") as file:
    file.write(first_name + "\n")
    file.write(last_name + "\n")

print("Program ending.")