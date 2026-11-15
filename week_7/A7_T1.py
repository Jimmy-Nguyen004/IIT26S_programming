# collect numbers
def collect_integer(numbers):
    print("Collect positive integers.")
    while True:
        number = int(input("Insert positive integer(negative stop): "))
        if number <= 0:
            break
        numbers.append(number)
    print("Stopped collecting positive integers.")
    return numbers

# display contents
def display_contents(numbers):
    if len(numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for i in range(len(numbers)):
            print(f"- Index {i} => Original {i + 1} => Integer {numbers[i]}")

# main function
def main():
    print("Program starting.")
    nums = []
    nums = collect_integer(nums)
    display_contents(nums)
    print("Program ending.")

main()