import A8_T7_lib as lib
import template as temp
from svgwrite import Drawing

def show_choices() -> None:
    print("Options:\n1 - Draw square\n2 - Draw circle\n3 - Draw hexagon\n4 - Save svg\n0 - Exit")
    return None

def main() -> None:
    print("Program starting.")
    dwg = Drawing()
    while True:
        show_choices()
        choice = temp.ask_choice()
        if choice == 1:
            lib.draw_square(dwg)
        elif choice == 2:
            lib.draw_circle(dwg)
        elif choice == 3:
            lib.draw_hexagon(dwg)
        elif choice == 4:
            lib.save_svg(dwg)
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