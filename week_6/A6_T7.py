lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

location = ["home", "Galba's palace", "Otho's palace", "Vitellius's palace", "Vespasian's palace"]
progress = "player_progress.txt"
# decipher function ROT13
def cipher(text):
    result = ""
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
    with open(progress, "r", encoding="utf-8") as file:
        lines = file.readlines()

    newest_row = lines[-1].strip() # read the last line [-1] and remove any trailing spaces

    parts = newest_row.split(";") # separate by ";"
    current_location = int(parts[0])
    next_location = int(parts[1])
    passphrase = parts[2]

    print("Currently at " + location[current_location] + ".")

    # check if there still somewhere else to go
    if next_location >= len(location):
        print("All messages have been gathered. Nowhere left to go.")
        print("Travel ending.")
        return

    # travel to other places
    print(f"Traveling to {location[next_location]}...")
    print(f"...Arriving to {location[next_location]}.")

    # pass the plain text to the guard
    plain_passphrase = cipher(passphrase)
    print("Passing the guard at the entrance.")
    print(f"\"{plain_passphrase.capitalize()}!\"")

    # open the ciphered message
    print("Looking for the message in the palace...")
    with open(str(next_location)+ "_" + passphrase +".gkg", "r", encoding="utf-8") as file:
        # File name: {Next_location}_{PassPhrase}.gkg
        first_line = file.readline()
        message = file.read()
    print("Ah, there it is! Seems cryptic.")

    # save progress to player_progress.txt
    with open(progress, "a", encoding="utf-8") as file:
        file.write(first_line.strip() + "\n")
    print("[Game] Progress autosaved!")

    # deciphering message
    print("Deciphering Emperor's message...")
    with open(str(next_location)+ "_" + plain_passphrase +".txt", "w", encoding="utf-8") as file:
        file.write(cipher(message))
    print("Looks like I've got now the plain version copy of the Emperor's message.")

    # finish 
    print("Time to leave...")
    print("Program ending.")

main()