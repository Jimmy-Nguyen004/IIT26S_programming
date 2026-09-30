def askDimension(PPrompt: str):
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth: float, PHeight: float):
   Area = PWidth * PHeight
   return Area

def main() -> None:
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calcRectangleArea(Width, Height)
    print("")
    print(f"Area is {Area}²")
    print("Program ending.")
    return None
main()