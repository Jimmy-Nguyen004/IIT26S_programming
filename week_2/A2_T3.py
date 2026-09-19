print("Program starting.")

firstword = input("Insert first word: ")
secondword = input("Insert second word: ")

print("1st word is", len(firstword), "characters long.")
print("2nd word is", len(secondword), "characters long.")

compound = firstword + secondword
print("Words together makes one closed compound '", compound, "'.", sep="")

print("Program ending.")