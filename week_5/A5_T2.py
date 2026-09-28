def frameWord(word):
    a = "*" * (len(word) + 4)
    print(a)
    print("*-" + word + "-*")
    print(a)
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print()
    print("Program ending.")
    return None

main()
    