WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()# 0. Clear PRows list just in case
    with open(PFilename, "r", encoding="utf-8") as Filehandle: # open filehandle
        Filehandle.readline() # skip first line
        for Line in Filehandle:
            if Line == "\n": # check if line is empty
                continue
            PRows.append(Line.rstrip("\n")) # add data rows to PRows
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(PRows)): # interate rows with i
        for j in range(len(WEEKDAYS)): # interate weekdays with k
            if PRows[i].startswith(WEEKDAYS[j]): # check if the row starts with the weekday name
                WeekdayTimestampAmount[j] += 1 # count the day in proper place
    for i in range(len(WEEKDAYS)): # iterate WEEKDAYS with i and append the daily results
        PResults.append(" - {} {} stamps".format(WEEKDAYS[i], WeekdayTimestampAmount[i]))
    WeekdayTimestampAmount.clear() # Clear the helper list
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    Rows: list[str] = [] # initialise rows list
    Results: list[str] = [] # initialise results list/*
    print("Program starting")
    Filename = input("Insert filename: ") # ask user to define filename
    readFile(Filename, Rows) # Read file
    analyseTimestamps(Rows, Results) # analyse rows
    displayResults(Results) # display results
    Rows.clear() # clean up
    Results.clear() # clear list
    print("Program ending")
    return None

main()