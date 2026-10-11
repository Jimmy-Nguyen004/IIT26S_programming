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
    Cel = float(input('Insert the amount of Celsius: '))
    Fah = (Cel * 1.8) + 32
    print(f"{Cel}°C equals to {round(Fah, 1)}°F")
elif choice == 2:
    Fah = float(input('Insert the amount of Fahrenheit: '))
    Cel = (Fah -32) / 1.8
    print(f"{Fah}°F equals to {round(Cel, 1)}°C")
else:
    print("Unknown option.")

print()
print("Program ending.")