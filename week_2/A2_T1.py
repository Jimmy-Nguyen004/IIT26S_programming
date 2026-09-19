print("Program starting.")

name = input("What is your name: ")
num1 = float(input("Enter a floating point number: "))
num2 = float(input("Enter second floating point number: "))

product = round((num1 * num2), 2)

print(f"{name} you gave numbers {num1} and {num2}")
print(f"Multiplying first and second number will give result in product {product}")

print("Program ending.")