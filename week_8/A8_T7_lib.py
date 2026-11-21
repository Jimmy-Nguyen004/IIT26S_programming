from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon
import math

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    left_pos = int(input("- Left edge position: "))
    top_pos = int(input("- Top edge position: "))
    length_side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(left_pos, top_pos), size=(length_side, length_side), fill=fill, stroke=stroke))
    return None

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    x_coord = int(input("- Center X coord: "))
    y_coord = int(input("- Center Y coord: "))
    radius = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(x_coord, y_coord), r=radius, fill=fill, stroke=stroke))
    return None

def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon")
    x_coord = int(input("- Center X coord: "))
    y_coord = int(input("- Center Y coord: "))
    apothem = int(input("- Apothem length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    # hexagon: r = a/cos(30)
    radius = apothem / math.cos(math.radians(30))

    points = []
    for i in range(6):
        # General Trigonometric Formulas
        x = round(x_coord + radius * math.cos(((math.pi / 2) + i * (math.pi / 3))))
        y = round(y_coord + radius * math.sin(((math.pi / 2) + i * (math.pi / 3))))
        points.append((x, y))

    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))
    return None

def saveSvg(PDwg: Drawing) -> None:
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