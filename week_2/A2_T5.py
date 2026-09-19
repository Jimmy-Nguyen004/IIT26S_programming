print("Program starting.")

print()

word = input("Insert a compound word: ")

reverse = word[::-1]
length = len(word)
last_char = word[-1]

print(f"The word you inserted is '{word}' and in reverse it is '{reverse}'.")
print(f"The inserted word length is {length}.")
print(f"Last character is '{last_char}'.")

print()

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
stop = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

substring = word[start:stop:step]

print()

print(f"The word '{word}' sliced to the defined substring is '{substring}'.")

print("Program ending.")