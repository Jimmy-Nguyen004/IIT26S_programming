from datetime import datetime

TIMESTAMPS_FORMAT = "%Y-%m-%dT%H:%M" # assign format string for timestamp

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def read_timestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()
    with open(PFilename, "r", encoding="UTF-8") as source:
        for row in source:
            row = row.strip()
            if row == "":
                continue
            PTimestamps.append(datetime.strptime(row, TIMESTAMPS_FORMAT))
    return None

def calc_timestamps_in_years(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if timestamp.year == PYear:
            count += 1
    return count

def calc_timestamps_in_months(PMonth: str, PTimestamps: list[datetime]) -> int:
    month = PMonth.capitalize() # bypass any incorrect input which leads to incorrect output
    if month not in MONTHS: # because
        return 0
    num_Of_Month = MONTHS.index(month) + 1
    count = 0
    for timestamp in PTimestamps:
        if timestamp.month == num_Of_Month:
            count += 1
    return count

def calc_timestamps_in_weekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    weekday = PWeekday.capitalize()
    if weekday not in WEEKDAYS:
        return 0
    num_of_Weekday = WEEKDAYS.index(weekday)
    count = 0
    for timestamp in PTimestamps:
        if timestamp.weekday() == num_of_Weekday:
            count += 1
    return count