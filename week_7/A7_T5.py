DELIMITER = ";"
class TimeStamp:
    weekday = ""
    hour = 0
    consumption = 0.0
    price = 0.0

class DayUsage:
    weekday = ""
    usage = 0.0
    cost = 0.0

def read_timestamps(PFilename: str, PTimestamps: list[TimeStamp]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear() # clear PTimestamps just in case
    with open(PFilename, "r", encoding="utf-8") as filehandle:
        filehandle.readline() # skip first line
        for line in filehandle:
            row = line.rstrip() # remove trailing spaces
            if len(row) == 0: # skip empty line
                continue
            Data = row.split(DELIMITER) # ["0", "1", "2", "3"]
            Timestamp = TimeStamp()
            Timestamp.weekday = Data[0]
            Timestamp.hour = int(Data[1])
            Timestamp.consumption = float(Data[2])
            Timestamp.price = float(Data[3])
            PTimestamps.append(Timestamp) # append Timestamp to big list PTimestamps
            Data.clear()
    return None

def analyse_timestamps(PTimestamps: list, PResults: list[str]) -> None:
    WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",)
    print("Analysing timestamps.")
    PResults.clear()
    DayUsages = [] # define DayUsages with a list
    for weekday in WEEKDAYS: # append every weekday in WEEKDAYS to big list DayUsages
        DayUsage = DayUsage() # create an object under name DayUsage
        DayUsage.weekday = weekday # append weekday to - weekday = "" - of class DAY_USAGE
        DayUsages.append(DayUsage)

    for Timestamp in PTimestamps: # check every timestamps in list PTimestamps
        for DayUsage in DayUsages: # check every DayUsage in list DayUsages []
            if Timestamp.weekday == DayUsage.weekday: # compare 2 variables of 2 object
                DayUsage.usage += Timestamp.consumption
                DayUsage.cost += Timestamp.consumption * Timestamp.price

    for DayUsage in DayUsages: # check each object in list DayUsage
        PResults.append(" - {} usage {:.2f} kWh, cost {:.2f} €".format(
            DayUsage.weekday, DayUsage.usage, DayUsage.cost)) # append content to list using each DayUsage data
    DayUsages.clear()
    return None

def display_results(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for Result in PResults:
        print(Result)
    print("### Electricity consumption summary ###")
    return None

def main():
    timestamps = []
    result: list[str] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    read_timestamps(filename, timestamps)
    analyse_timestamps(timestamps, result)
    display_results(result)
    timestamps.clear()
    result.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
