# parse the input
def parse_input(string):
    numbers = []
    values = string.split(",")
    for value in values:
        if value.isdigit():
            number = int(value)
            numbers.append(number)
        else:
            print(f"Invalid value {value} detected.")
    return numbers

# analyse valid integer
def analyse_content(numbers):
    if len(numbers) == 0:
        print("No values to analyse.")
    total = sum(numbers)
    print(f"There are {len(numbers)} integers in the list.")
    if total % 2 == 0:
        print(f"Sum of the integers is {total} and it's even.")
    else:
        print(f"Sum of the integers is {total} and it's odd.")

# main function
def main():
    print("Program starting.")
    string = input("Insert comma separated integers: ")
    nums = parse_input(string)
    analyse_content(nums)
    print("Program ending.")

main()