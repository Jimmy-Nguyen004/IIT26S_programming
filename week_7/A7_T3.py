WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def read_file(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()# 0. Clear PRows list just in case
    with open(PFilename, "r", encoding="utf-8") as filehandle: # open filehandle
        filehandle.readline() # skip first line
        for Line in filehandle:
            if Line == "\n": # check if line is empty
                continue
            PRows.append(Line.rstrip("\n")) # add data rows to PRows
    return None

def analyse_timestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    weekday_timestamp_amount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(PRows)): # iterate rows with i
        for j in range(len(WEEKDAYS)): # iterate weekdays with k
            if PRows[i].startswith(WEEKDAYS[j]): # check if the row starts with the weekday name
                weekday_timestamp_amount[j] += 1 # count the day in proper place
    for i in range(len(WEEKDAYS)): # iterate WEEKDAYS with i and append the daily results
        PResults.append(" - {} {} stamps".format(WEEKDAYS[i], weekday_timestamp_amount[i]))
    weekday_timestamp_amount.clear() # Clear the helper list
    return None

def display_results(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    rows: list[str] = [] # initialise rows list
    results: list[str] = [] # initialise results list/*
    print("Program starting")
    filename = input("Insert filename: ") # ask user to define filename
    read_file(filename, rows) # Read file
    analyse_timestamps(rows, results) # analyse rows
    display_results(results) # display results
    rows.clear() # clean up
    results.clear() # clear list
    print("Program ending")
    return None

main()