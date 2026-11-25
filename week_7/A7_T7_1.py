'''
Enigma Machine (with class)
'''
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ":"

class ENIGMA:
    rotors = []
    positions = []
    reflector = ""

def read_config(PFilename: str, PEnigma: ENIGMA) -> None:
    PEnigma.rotors.clear()
    with open(PFilename, "r", encoding="UTF-8") as filehandle:
            for line in filehandle:
                row = line.rstrip()
                if len(row) == 0:
                    continue
                data = row.split(DELIMITER)
                if data[0].startswith("Rotor"):
                    PEnigma.rotors.append(data[1])
                elif data[0].startswith("Reflector"):
                    PEnigma.reflector = data[1]
            return None

def rotate_rotors(PEnigma: ENIGMA) -> None:
    PEnigma.positions[0] += 1
    if PEnigma.positions[0] == 26:
        PEnigma.positions[0] = 0
        PEnigma.positions[1] += 1
    if PEnigma.positions[1] == 26:
        PEnigma.positions[1] = 0
        PEnigma.positions[2] += 1
    if PEnigma.positions[2] == 26:
        PEnigma.positions[2] = 0
    return None

def forward_run(PEnigma: ENIGMA, PChar: str) -> str:
    char = PChar
    for i in range(len(PEnigma.rotors)):
        rotor = PEnigma.rotors[i]
        position = PEnigma.positions[i]
        number = Alphabet.index(char) + position
        if number >= 26:
            number -= 26
        shifted_char = Alphabet[number]
        number = rotor.index(shifted_char)
        number -= position
        if number < 0:
            number += 26
        char = Alphabet[number]
    return char

def reversed_run(PEnigma: ENIGMA, PChar: str) -> str:
    char = PChar
    for i in range(len(PEnigma.rotors) -1, -1, -1):
        rotor = PEnigma.rotors[i]
        position = PEnigma.positions[i]
        number = Alphabet.index(char) + position
        if number >= 26:
            number -= 26
        wired_char = rotor[number]
        number = Alphabet.index(wired_char) - position
        if number < 0:
            number += 26
        char = Alphabet[number]
    return char

def reflector(PEnigma: ENIGMA, PChar: str) -> str:
    return PEnigma.reflector[Alphabet.index(PChar)]

def scramble_char(PEnigma: ENIGMA, PChar: str) -> str:
    if PChar not in Alphabet:
        return PChar
    rotate_rotors(PEnigma)
    char = forward_run(PEnigma, PChar)
    char = reflector(PEnigma, char)
    char = reversed_run(PEnigma, char)
    return char

def main():
    machine = ENIGMA()
    machine.rotors = []
    machine.positions = [0,0,0]
    filename = input("Insert config(filename): ")
    read_config(filename, machine)
    input("Insert plugs (y/n)?: ")
    print("No extra plugs inserted.")
    print("Enigma initialized.")
    while True:
        print()
        row = input("Insert row (empty stops): ")

        if len(row) == 0:
            break

        machine.positions[0] = 0
        machine.positions[1] = 0
        machine.positions[2] = 0

        converted = ""

        for char in row:
            new_char = scramble_char(machine, char)
            print('Character "{}" illuminated as "{}"'.format(char, new_char))
            converted += new_char
        print('Converted row - "{}".'.format(converted))

    print()
    print("Enigma closing.")
    machine.rotors.clear()
    machine.positions.clear()
    return None

if __name__ == "__main__":
    main()