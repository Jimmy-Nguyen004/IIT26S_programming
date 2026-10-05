SEPERATOR = ","
#read values function
def readValues(filename) -> str:
    values = ""
    with open(f'week_6/files/{filename}', "r", encoding="UTF-8") as source:
        for line in source:
            value = line.strip()
            if value == "":
                continue
            if values == "":
                values = value
            else:
                values += SEPERATOR + value
        return values

#analysing values function
def analyseValues(values) -> str:
    numbers = values.split(SEPERATOR) if values != 0 else []
    count = 0
    sum = 0
    greater = 0
    for number in numbers:
        value = int(number)
        count += 1
        sum += value
        if value > greater:
            greater = value
    average = sum / count if count > 0 else 0

    result = str(count) + ";"
    result += str(sum) + ";"
    result += str(greater) + ";"
    result += str(average)
    return result
#displaying function
def displayingValues(filename, result):
    print("#### Number analysis - START ####")
    print(f'File {filename} results:')
    print("Count;Sum;Greatest;Average")
    print(result)
    print()
    print("#### Number analysis - END ####")
    return None

#main function
print("Program starting.")
filename = input("Insert filename: ")
values = readValues(filename)
result = analyseValues(values)
displayingValues(filename, result)
print("Program ending.")
