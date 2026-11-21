import A8_T6_lib as lib
import template as temp
from svgwrite import Drawing

def showChoices() -> None:
    print("Options:\n1 - Draw square\n2 - Draw circle\n3 - Save svg\n0 - Exit")
    return None

def main() -> None:
    print("Program starting.")
    Dwg = Drawing()
    while True:
        showChoices()
        choice = temp.askChoice()
        if choice == 1:
            lib.drawSquare(Dwg)
        elif choice == 2:
            lib.drawCircle(Dwg)
        elif choice == 3:
            lib.saveSvg(Dwg)
        elif choice == 0:
            print("Exiting program.")
            print()
            break
        else:
            print("Unknown choice!")
        print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()