DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

class Timestamp:
    weekday = ""
    sum = 0
    consumption = 0.0
    price = 0.0

class Day_usage:
    weekday = ""
    usage = 0.0
    cost = 0.0

def readTimestamps(PFilename: str, PTimestamps: list[Timestamp]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear() # clear PTimestamps just in case
    with open(PFilename, "r", encoding="utf-8") as Filehandle:
        Filehandle.readline() # skip first line
        for Line in Filehandle:
            Row = Line.rstrip()
            if len(Row) == 0: # skip empty line
                continue
            Column = Row.split(DELIMITER)
            TIMESTAMP = Timestamp()
            TIMESTAMP.weekday = Column[0]
            TIMESTAMP.hour = int(Column[1])
            TIMESTAMP.consumption = float(Column[2])
            TIMESTAMP.price = float(Column[3])
            PTimestamps.append(TIMESTAMP)
            Column.clear()
    return None

def analyseTimestamps(PTimestamps: list, PResult: list[str]) -> None:
    print("Analysing timestamps.")
    PResult.clear()
    