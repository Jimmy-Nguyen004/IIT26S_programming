########################################################
# Task A9_T4
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")
    try:
        Celsius = float(feed)
    except ValueError:
        print("could not convert string to float: '{}'".format(feed))
        return None
    if Celsius < TEMP_MIN or Celsius > TEMP_MAX:
        print("{} temperature out of range.".format(feed))
        return None
    return Celsius

def main() -> None:
    print("Program starting.")
    Celsius = collectCelsius()
    if Celsius is not None:
        print(f"You inserted {Celsius} °C")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()