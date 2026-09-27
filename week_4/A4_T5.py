print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

condition = True
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    condition = False
if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop")
    condition = False

if condition == True:
    print("\nFirst loop - inspection with break")
    first_char = True
    for i in range(start, inspection):
        if i == inspection:
            break
        if first_char:
            first_char = False
        else:
            print(" ", end="")
        print(i, end="")
    print()

    print("Second loop - inspection will continue:")
    first_char = True
    for i in range(start, stop):
        if i == inspection:
            continue
        if first_char:
            first_char = False
        else:
            print(" ", end="")
        print(i, end="")
    print()

print("\nProgram ending")