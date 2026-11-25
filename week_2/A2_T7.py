print("Program starting.")
fahrenheit = float(input("Insert fahrenheit: "))
celsius = round((fahrenheit - 32) / 1.8, 1)

print(f"{fahrenheit}°F is {celsius:.1f}°C")
print("Program ending.")