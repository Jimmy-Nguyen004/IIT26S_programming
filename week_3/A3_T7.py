print("Program starting.")
print("Testing decision structures.")
value = int(input("Insert an integer: "))

print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print("Using one multi-branched decision structure.")
    if value >= 400:
        value += 44
    elif value >= 200:
        value += 22
    elif value >= 100:
        value += 11
    print(f"Result is {value}")
elif choice == 2:
    print("Using multiple independent if-statements structure.")
    if value >= 400:
        value += 44
    if value >= 200:
        value += 22
    if value >= 100:
        value += 11
    print(f"Result is {value}")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print()

print("Program ending.")