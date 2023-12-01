import re

map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import re

def part1():
    # Read the file and get all the lines
    with open('Day01/Input') as f:
        lines = f.readlines()

    # Loop through each line and retrieve the first and last digit
    for i in range(len(lines)):
        temp_result = re.findall(r'\d', lines[i])
        temp_result = [temp_result[0], temp_result[-1]]
        lines[i] = int("".join(temp_result))

    # Print the sum of all the digits
    print(sum(lines))

def part2():

    # Read in the file
    with open('Day01/Input') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        # Extract digits and written numbers from the line
        temp_result_str = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', lines[i])
        temp_result = []
        for str_num in temp_result_str:
            # Map word numbers to digits if they are not already digits
            if str_num not in nums:
                temp_result.append(map[str_num])
            else:
                temp_result.append(str_num)
        # Take the first and last element of the resulting list
        temp_result = [temp_result[0], temp_result[-1]]
        # Replace the line with the calculated number
        lines[i] = int("".join(temp_result))

    # Calculate and print the sum of the calculated numbers
    print(sum(lines))

if __name__ == '__main__':
    part1()
    part2()