DELIMITER = ","

def collectWords():
    words = ""
    while True:
        word = input("Insert word (empty stop): ")
        if word == "":
            break
        if words == "":
            words = word
        else:
            words = words + DELIMITER + word
    return words

def analyseWords(words):
    if words == "":
        wordList = []
    else:
        wordList = words.split(DELIMITER)

    wordCount = len(wordList)
    char = 0
    for word in wordList:
        char += len(word)

    if wordCount > 0:
        wordAverage = char / wordCount
    else:
        wordAverage = 0
    print("- {} Words".format(wordCount))
    print("- {} Characters".format(char))
    print("- {:.2f} Average word length".format(wordAverage))

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    return None
main()
