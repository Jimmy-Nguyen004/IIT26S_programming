print("Program starting.\n")
 
print("Check multiplicative persistence.")
number = int(input("Insert an integer: "))
steps = 0

while len(str(number)) > 1:
    product = 1
    first_char = True
    for digit in str(number):
        if first_char:
            first_char = False
        else:
            print(" * ", end="")
        print(digit, end="")
        product *= int(digit)
    print(f" = {product}")
    number = product
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")