print("Program starting.\n")

word_count = 0
char_count = 0

word = input("Insert word (empty stop): ")
while word != "":
    word_count += 1
    char_count += len(word)
    word = input("Insert word (empty stop): ")

print("\nYou inserted:")
print(f"- {word_count} words")
print(f"- {char_count} characters")

print("\nProgram ending.")