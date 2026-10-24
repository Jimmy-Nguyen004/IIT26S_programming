lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

location = ["home", "Galba's palace", "Otho's palace", "Vitellius's palace", "Vespasian's palace"]
progress = "player_progress.txt"
# decipher function
def  cipher(text):
    for char in text:
        if char in lower:
            i = lower.find(char)
            i = i + 13
            if i >= 26:
                i = i - 26
            result = result + lower[i]
        elif char in upper:
            i = lower.find(char)
            i = i + 13
            if i >= 26:
                i = i - 26
            result = result + upper[i]
        else:
            result = result + char
        return result

# main function
def main():
    print("Travel starting.")

    # read the newest row
    file = open(progress, "r")
    lines = file.readlines()
    file.close()
    newest_row = lines[-1].strip()
    parts = newest_row.split(";")
    current_location = int(parts[0])
    next_location = int(parts[1])
    passpharse = parts[2]

    print("Currently at " + location[current_location] + ".")

    # check if there still somewhere else to go

    # pass the plain text to the guard

    # open the ciphered message

    #