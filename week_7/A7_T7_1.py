'''
Enigma Machine (with class)
'''
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ":"

class ENIGMA:
    rotors = []
    positions = []
    reflector = ""

def readConfig(PFilename: str, PEnigma: ENIGMA) -> None:
    PEnigma.rotors.clear()
    with open(PFilename, "r", encoding="UTF-8") as Filehandle:
            for Line in Filehandle:
                Row = Line.rstrip()
                if len(Row) == 0:
                    continue
                data = Row.split(DELIMITER)
                if data[0].startswith("Rotor"):
                    PEnigma.rotors.append(data[1])
                elif data[0].startswith("Reflector"):
                    PEnigma.reflector = data[1]
            return None

def rotateRotors(PEnigma: ENIGMA) -> None:
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

def forwardRun(PEnigma: ENIGMA, PChar: str) -> str:
    Char = PChar
    for i in range(len(PEnigma.rotors)):
        Rotor = PEnigma.rotors[i]
        Position = PEnigma.positions[i]
        Number = Alphabet.index(Char) + Position
        if Number >= 26:
            Number -= 26
        shiftedChar = Alphabet[Number]
        Number = Rotor.index(shiftedChar)
        Number -= Position
        if Number < 0:
            Number += 26
        Char = Alphabet[Number]
    return Char

def reversedRun(PEnigma: ENIGMA, PChar: str) -> str:
    Char = PChar
    for i in range(len(PEnigma.rotors) -1, -1, -1):
        Rotor = PEnigma.rotors[i]
        Position = PEnigma.positions[i]
        Number = Alphabet.index(Char) + Position
        if Number >= 26:
            Number -= 26
        wiredChar = Rotor[Number]
        Number = Alphabet.index(wiredChar) - Position
        if Number < 0:
            Number += 26
        Char = Alphabet[Number]
    return Char

def reflector(PEnigma: ENIGMA, PChar: str) -> str:
    return PEnigma.reflector[Alphabet.index(PChar)]

def scrambleChar(PEnigma: ENIGMA, PChar: str) -> str:
    if PChar not in Alphabet:
        return PChar
    rotateRotors(PEnigma)
    Char = forwardRun(PEnigma, PChar)
    Char = reflector(PEnigma, Char)
    Char = reversedRun(PEnigma, Char)
    return Char

def main():
    Machine = ENIGMA()
    Machine.rotors = []
    Machine.positions = [0,0,0]
    Filename = input("Insert config(filename): ")
    readConfig(Filename, Machine)
    input("Insert plugs (y/n)?: ")
    print("No extra plugs inserted.")
    print("Enigma initialized.")
    while True:
        print()
        Row = input("Insert row (empty stops): ")

        if len(Row) == 0:
            break

        Machine.positions[0] = 0
        Machine.positions[1] = 0
        Machine.positions[2] = 0

        converted = ""

        for Char in Row:
            newChar = scrambleChar(Machine, Char)
            print('Character "{}" illuminated as "{}"'.format(Char, newChar))
            converted += newChar
        print('Converted row - "{}".'.format(converted))

    print()
    print("Enigma closing.")
    Machine.rotors.clear()
    Machine.positions.clear()
    return None

if __name__ == "__main__":
    main()