DELIMETER = ";"

class Timestamp:
    weekday = ""
    hour = 0
    consumption = 0.0
    price = 0.0

def readTimestamps(PFilename: str, PTimestamps: list[Timestamp]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear() # clear PTimestamps just in case
    with open(PFilename, "r", encoding="utf-8") as Filehandle:
        Filehandle.readline() # skip first line
        for Line in Filehandle:
            Row = Line.rstrip()
            if len(Row) == 0: # skip empty line
                continue
            Column = Row.split(DELIMETER)
            TIMESTAMP = Timestamp()
            TIMESTAMP.weekday = Column[0]
            TIMESTAMP.hour = int(Column[1])
            TIMESTAMP.consumption = float(Column[2])
            TIMESTAMP.price = float(Column[3])
            PTimestamps.append(TIMESTAMP)
            Column.clear()
    return None

def displayTimestamp(PTimestamps: list[Timestamp]) -> None:
    print("Electricity usage:")
    for TIMESTAMP in PTimestamps:
        Total = TIMESTAMP.consumption * TIMESTAMP.price
        print(" - {} {:02d}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
            TIMESTAMP.weekday, TIMESTAMP.hour, TIMESTAMP.price, TIMESTAMP.consumption, Total))
    return None

def main():
    Timestamps: list[Timestamp] = []
    print("Program starting")
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Timestamps)
    displayTimestamp(Timestamps)
    Timestamps.clear()
    print("Program ending")
    return None

main()