print("Program starting.")
print("String comparisons")

word_first = input("Insert first word: ")
character = input("Insert a character: ")

if character in word_first:
    print(f'Word "{word_first}" contains character "{character}"')
else:
    print(f'Word "{word_first}" doesn\'t contain character "{character}"')

word_second = input("Insert second word: ")

if word_first < word_second:
    print(f'The first word "{word_first}" is before the second word "{word_second}" alphabetically.')
elif word_first > word_second:
    print(f'The second word "{word_second}" is before the first word "{word_first}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{word_first}"')

print("Program ending.")