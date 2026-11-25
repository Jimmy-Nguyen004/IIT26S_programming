print("Program starting")
print()

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 0:
    print("Exiting...")
elif choice == 1:
    cel = float(input('Insert the amount of Celsius: '))
    fah = (cel * 1.8) + 32
    print(f"{cel}°C equals to {round(fah, 1)}°F")
elif choice == 2:
    fah = float(input('Insert the amount of Fahrenheit: '))
    cel = (fah -32) / 1.8
    print(f"{fah}°F equals to {round(cel, 1)}°C")
else:
    print("Unknown option.")

print()
print("Program ending.")