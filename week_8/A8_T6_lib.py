from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon

def draw_square(PDwg: Drawing) -> None:
    print("Insert square")
    left_pos = int(input("- Left edge position: "))
    top_pos = int(input("- Top edge position: "))
    length_side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(left_pos, top_pos), size=(length_side, length_side), fill=fill, stroke=stroke))
    return None

def draw_circle(PDwg: Drawing) -> None:
    print("Insert circle")
    x_coord = int(input("- Center X coord: "))
    y_coord = int(input("- Center Y coord: "))
    radius = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(x_coord, y_coord), r=radius, fill=fill, stroke=stroke))
    return None

def save_svg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print('Saving file to "{}"'.format(filename))
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        PDwg.filename = filename
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")
    elif proceed.lower() == "n":
        print("Vector saving cancelled!")
    else:
        print("Unknown choice!")
    return None