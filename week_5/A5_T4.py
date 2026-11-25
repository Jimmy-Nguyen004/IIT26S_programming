def ask_dimensions(PPrompt: str) ->float:
   feed = float(input(f"Insert {PPrompt}: "))
   return feed

def calc_rectangle_area(PWidth: float, PHeight: float) ->float:
   area = PWidth * PHeight
   return area

def main():
    print("Program starting.")
    width = ask_dimensions("width")
    height = ask_dimensions("height")
    area = calc_rectangle_area(width, height)
    print("")
    print(f"Area is {area}²")
    print("Program ending.")
    return None
main()