def read_names(filename: str)-> str:
    print(f'Reading names from "{filename}".')
    names= ""
    with open(f"week_6/files/{filename}", "r", encoding="UTF-8") as source:
        for line in source:
            name = line.strip()
            if name == "":
                continue
            if names == "":
                names = name
            else:
                names += ";" + name
    return names

def analyse_names(names: str)-> str:
    print("Analysing names...")
    namelist = names.split(";") if names != "" else []
    count = len(namelist)
    shortest = 0
    longest = 0
    total_length = 0
    for name in namelist:
        length = len(name)
        total_length += length
        if shortest == 0 or length < shortest:
            shortest = length
        if length > longest:
            longest = length
    average = total_length / count if count > 0 else 0
    print("Analysis complete!")

    report = "#### REPORT BEGIN ####\n"
    report += "Name count - {}\n".format(count)
    report += "Shortest name - {} chars\n".format(shortest)
    report += "Longest name - {} chars\n".format(longest)
    report += "Average name - {:.2f} chars\n".format(average)
    report += "#### REPORT END ####"
    return report

def main() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    names = read_names(filename)
    report = analyse_names(names)
    print(report)
    print("Program ending.")
    return None

main()