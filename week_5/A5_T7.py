DELIMITER = ","

def collect_words():
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

def analyse_words(words):
    if words == "":
        word_list = []
    else:
        word_list = words.split(DELIMITER)

    word_count = len(word_list)
    char = 0
    for word in word_list:
        char += len(word)

#    if wordCount > 0:
#        wordAverage = char / wordCount
#    else:
#        wordAverage = 0
    word_average = char / word_count if word_count > 0 else 0
    
    print("- {} Words".format(word_count))
    print("- {} Characters".format(char))
    print("- {:.2f} Average word length".format(word_average))

def main():
    print("Program starting.")
    words = collect_words()
    analyse_words(words)
    return None
main()
