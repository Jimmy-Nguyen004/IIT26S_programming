print("Program starting.")

first_word = input("Insert first word: ")
second_word = input("Insert second word: ")

print("1st word is", len(first_word), "characters long.")
print("2nd word is", len(second_word), "characters long.")

compound = first_word + second_word
#print("Words together makes one closed compound '", compound, "'.", sep="")
print(f"Words together makes one closed compound \'{compound}\'.")

print("Program ending.")