print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print()

print("Options: ")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 0:
    print()
    print("Exiting...")
elif choice == 1:
    print()
    print("Length options: ")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    sub_choice = int(input("Your choice: "))
    if sub_choice == 0:
        print("Exiting...")
    elif sub_choice == 1:
        m = float(input("Insert meters: "))
        km = m * 0.001
        print(f"{round(m, 1)} m is {round(km, 1)} km")
    elif sub_choice == 2:
        km = float(input("Insert kilometers: "))
        m = km * 1000.0
        print(f"{round(km, 1)} km is {round(m, 1)} m")
    else:
        print("Unknown option.")
elif choice == 2:
    print()
    print("Weight options: ")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    sub_choice = int(input("Your choice: "))
    if sub_choice == 0:
        print("Exiting...")
    elif sub_choice == 1:
        g = float(input("Insert grams: "))
        lb= g * 0.002205
        print(f"{round(g, 1)} g is {round(lb, 1)} lb")
    elif sub_choice == 2:
        lb = float(input("Insert pounds: "))
        g= lb * 453.6
        print(f"{round(lb, 1)} lb is {round(g, 1)} g")
    else:
        print("Unknown option.")
else:
    print("Unknown option.")
print()

print("Program ending.")