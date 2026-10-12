print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for i in range(start, stop + 1):
    if i < stop:
        print(i, end=" ")
    else:
        print(i)

print("\nProgram ending.")
