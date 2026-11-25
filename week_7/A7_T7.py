'''
The program must handle:

3 x Rotors with 26 positions (A-Z)
1 x Reflector - Types A, B & C
0 x Plugboard. Prompt is required, but no need to implement.
The order of machine operations described:

User presses letter on the keyboard
Keypress is passed via plugboard (skipped in this exercise)
Rotate the wheels (positions)
Scramble current letter using “Forward pass-through” process
Iterate through rotors in order 1-3
Create offset using current rotor position and the letter
Use the offset to shift the given letter in alphabets
Scramble current letter using using the reflector
Scramble current letter using “Reverse pass-through” process
Iterate through rotors in reverse order
Change current letter based on each wheel position offset
In this program, user inserts row and the scrambling starts always from positions [0, 0, 0]. So enter press means that the program must reset the positions before scrambling the inserted text. The Enigma machine will shut down if the user enters an empty line.

Recommended datastructures:

Rotors(characters): list[str]
Positions(rotor positions): list[int]
Reflector: str
'''

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ":"

# no idea!
def read_config(PFilename: str, PRotors: list[str]) -> str:
    PRotors.clear()
    reflector = ""
    with open(PFilename, "r", encoding="UTF-8") as filehandle:
        for line in filehandle:
            # remove the line break and trailing spaces
            row = line.rstrip()
            if len(row) == 0:
                continue
            data = row.split(DELIMITER) # cut the string by the colon, turn into list -> ["Rotor1", "..."]
            if data[0].startswith("Rotor"): # check and append rotors' config to PRotors
                PRotors.append(data[1])
            elif data[0].startswith("Reflector"): # check and append reflector's config to Reflector
                reflector = data[1]
        return reflector

def rotate_rotors(PPositions: list[int]) -> None: 
    PPositions[0] += 1 # PPositions = [1,0,0]
    if PPositions[0] == 26: # if the position of the rotor 1 is full 26
        PPositions[0] = 0 # reset the rotor 1 to 0
        PPositions[1] += 1 # turn position of rotor 2 by 1 index
    if PPositions[1] == 26:
        PPositions[1] = 0
        PPositions[2] += 1
    if PPositions[2] == 26:
        PPositions[2] = 0
    return None

'''
Idea: The signal from the pressed button will reach the spot on the rotor, but the rotor is turned 
so the code have to + position (of the rotor at the moment), then the code will pick up that letter and find it in
'''
def forward_run(PRotors: list[str], PPositions: list[int], PChar: str) -> str:
    char = PChar
    for i in range(len(PRotors)):
        # Rotor means choose the rotor number i from PRotors -> return a string from the config
        rotor = PRotors[i]
        # PPositions = [1,0,0] at the start of the run, then [2,0,0] for the second loop,...
        position = PPositions[i] # -> how far the rotor i has turned
        # Letter -> Index num + position -> Shifted letter (because the rotor turned)
        number = Alphabet.index(char) + position
        if number >= 26: # if it pass the last index of the last letter (z)
            number -= 26 # subtract 26 to find the real index
        # look up to the original alphabet to find the letter base on the number
        shifted_char = Alphabet[number]
        # find the shifted char in the config and return the index of that letter in the config
        number = rotor.index(shifted_char)
        number -= position # - position because the rotor has turned
        if number < 0: # fix the negative number
            number += 26 # add 26 to continue from Z
        # reassign letter with the new index base on the original alphabet (prepared for the next loop)
        char = Alphabet[number]
    return char

# Same idea as the forwardPass function but reversed
def reversed_run(PRotors: list[str], PPositions: list[int], PChar: str) -> str:
    # Char = the letter coming back from the reflector
    char = PChar
    # go through the rotors backwards: i = 2, 1, 0 -> rotor 3, rotor 2, rotor 1
    for i in range(len(PRotors) -1, -1, -1):
        # Rotor = the config string of rotor i
        rotor = PRotors[i]
        # how far rotor i is turned
        position = PPositions[i]
        # step 1: shift character based on rotor position
        # Letter -> Index num + position -> the spot the signal hits (because the rotor turned)
        number = Alphabet.index(char) + position
        if number >= 26: # if it passes the last index of the last letter (Z)
            number -= 26 # subtract 26 to continue from A
        # (opposite of forwardRun, which searches for the letter's index)
        wiredChar = rotor[number]
        # step 3: letter -> index num, then - position because the rotor has turned
        number = Alphabet.index(wiredChar) - position
        if number < 0: # fix the negative number
            number += 26 # add 26 to continue from Z
        # reassign letter with the new index based on the original alphabet (prepared for the next loop)
        char = Alphabet[number]
    return char

def reflector(PReflector: str, PChar: str) -> str:
    return PReflector[Alphabet.index(PChar)]

def scramble_char(PRotors: list[str], PPositions: list[int], PReflector: str, PChar: str) -> str:
    # check for spaces, any non-alphabetical letter
    if PChar not in Alphabet:
        return PChar
    rotate_rotors(PPositions)
    char = forward_run(PRotors, PPositions, PChar) # rotors: 1 -> 2 -> 3
    char = reflector(PReflector, char) # reflector
    char = reversed_run(PRotors, PPositions, char) # rotors: 3 -> 2 -> 1
    return char

def main():
    rotors: list[str] = []
    positions: list[int] = [0,0,0]
    filename = input("Insert config(filename): ")
    reflector = read_config(filename, rotors)
    input("Insert plugs (y/n)?: ")
    print("No extra plugs inserted.")
    print("Enigma initialized.")
    while True:
        print()
        row = input("Insert row (empty stops): ")

        if len(row) == 0:
            break

        positions[0] = 0
        positions[1] = 0
        positions[2] = 0

        converted = ""

        for char in row:
            new_char = scramble_char(rotors, positions, reflector, char)
            print('Character "{}" illuminated as "{}"'.format(char, new_char))
            converted += new_char
        print('Converted row - "{}".'.format(converted))

    print()
    print("Enigma closing.")
    rotors.clear()
    positions.clear()
    return None

if __name__ == "__main__":
    main()