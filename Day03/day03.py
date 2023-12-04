def part1():
    # Read in Input
    with open('Day03/input.txt') as f:
        lines = f.readlines()
        lines = [line.split('\n')[0] for line in lines]
    blanc_string = "." * len(lines[0])
    # prepare the mask (* for adjacent, . for not adjacent)
    mask = [blanc_string] * len(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not (lines[i][j].isdigit()) and lines[i][j] != '.':
                lower_bound_i = max(0, i - 1)
                upper_bound_i = min(len(lines), i + 2)
                lower_bound_j = max(0, j - 1)
                upper_bound_j = min(len(lines[i]), j + 2)
                for l in range(lower_bound_i, upper_bound_i):
                    mask[l] = mask[l][:j - 1] + ('*' * (upper_bound_j - lower_bound_j)) + mask[l][j + 2:]
    # Get all the numbers
    sum = 0
    num_state = False
    for i in range(len(lines)):
        # edgecase, if a number was at the end of the previous line
        if num_state:
            is_adjacent = True if "*" in mask[i - 1][start_idx:j] else False
            sum += int(temp_number) if is_adjacent else 0
        start_idx = -1
        temp_number = ""
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                temp_number += lines[i][j]
                start_idx = j if start_idx == -1 else start_idx
                num_state = True
            elif not lines[i][j].isdigit() and num_state:
                is_adjacent = True if "*" in mask[i][start_idx:j] else False
                sum += int(temp_number) if is_adjacent else 0
                temp_number = ""
                num_state = False
                start_idx = -1
    print(sum)
    

def part2():
    # Read in Input
    with open('Day03/input.txt') as f:
        lines = f.readlines()
        lines = [line.split('\n')[0] for line in lines]
    num_values = 0
    sum = 0
    temp_values = 1
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                lower_bound_i = max(0, i - 1)
                upper_bound_i = min(len(lines), i + 2)
                lower_bound_j = max(0, j - 1)
                upper_bound_j = min(len(lines[i]), j + 2)
                for l in range(lower_bound_i, upper_bound_i):
                    found_number = False
                    for k in range(lower_bound_j, upper_bound_j):
                        if lines[l][k].isdigit() and not found_number:
                            found_number = True
                            num_values += 1
                            temp_values *= get_full_number(lines, l, k)
                        elif not lines[l][k].isdigit() and found_number:
                            found_number = False
                sum += temp_values if num_values == 2 else 0
                temp_values = 1
                num_values = 0
    print(sum)

def get_full_number(lines: list, i: int, j: int) -> int:
    start_idx = j
    # Lazy Evaluation, otherwise this would be an IndexError in case of start_idx == 0
    while start_idx != 0 and lines[i][start_idx - 1].isdigit():
        start_idx -= 1
    stop_index = j
    while stop_index != len(lines[i]) - 1 and lines[i][stop_index + 1].isdigit():
        stop_index += 1
    return int(lines[i][start_idx:stop_index + 1])


if __name__ == '__main__':
    part1()
    part2()