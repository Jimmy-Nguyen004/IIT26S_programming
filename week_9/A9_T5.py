########################################################
# Task A9_T5
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

BYTE_MIN = 0
BYTE_MAX = 255

def collect_bytes(PPrompt: str) -> int:
    try: 
        value = int(PPrompt)
    except ValueError:
        print('"{}" is a non numeric value.'.format(PPrompt))
        raise ValueError
    if value < BYTE_MIN or value > BYTE_MAX:
        print('Value "{}" is out of the range 0-255.'.format(value))
        raise ValueError
    return value

def showBytes(PRed: int, PGreen: int, PBlue: int):
    print("RGB Details: \n- Red {}\n- Green {}\n- Blue {}".format(PRed, PGreen, PBlue))
    print("- Hex #{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue))

def main():
    print("Program starting.")
    try:
        red = input("Insert red: ")
        red = collect_bytes(red)
        green = input("Insert green: ")
        green = collect_bytes(green)
        blue = input("Insert blue: ")
        blue = collect_bytes(blue)
        showBytes(red, green, blue)
    except ValueError:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()