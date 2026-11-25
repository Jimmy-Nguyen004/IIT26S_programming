########################################################
# Task A9_T4
# Developer: Nguyen Cat Duc Khiem
# Date: 21/11/2026
########################################################

temp_min = -273.15
temp_max = 10000

def collect_celsius():
    feed = input("Insert Celsius: ")
    try:
        cel = float(feed)
    except ValueError:
        print("could not convert string to float: '{}'".format(feed))
        return None
    if cel < temp_min or cel > temp_max:
        print("{} temperature out of range.".format(feed))
        return None
    return cel

def main() -> None:
    print("Program starting.")
    celsius = collect_celsius()
    if celsius is not None:
        print(f"You inserted {celsius} °C")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()