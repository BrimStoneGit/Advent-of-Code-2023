def read_input():
    with open('Day05/input.txt') as f:
        lines = f.readlines()
        lines = [line.split('\n')[0] for line in lines]
    return lines

def format_seeds(seed_line: str):
    seed_line = seed_line.split(": ")[1]
    return [int(seed) for seed in seed_line.split(" ")]
    

def split_list_at_empty(original_list: list):
    result = []
    sublist = []

    for item in original_list:
        if item == '':
            if sublist:
                result.append(sublist)
                sublist = []
        else:
            sublist.append(item)
            
    if sublist:
        result.append(sublist)

    return result

# Class to execute a bunch of functions onto a value
# Add functions via add_func(), execute via map()
class MappingClass:
    def __init__(self):
        self.mapping_funcs = []

    def add_func(self, new_func):
        self.mapping_funcs.append(new_func)
    
    def map(self, x):
        for func in self.mapping_funcs:
            result = func(x)
            if result[1]:
                return result[0]
        return x


def build_function(input: str):
    input = input.split(" ")
    dst_index = int(input[0])
    source_index = int(input[1])
    length = int(input[2])
    def func(x: int):
        if x >= source_index and x < source_index + length:
            return (x + (dst_index - source_index), True)
        else:
            return (x, False)
    return func


def part1():
    input = read_input()
    seed_list = format_seeds(input[0])
    mapping_list = split_list_at_empty(input[2:])
    mapping_list = [map[1:] for map in mapping_list]
    mapping_classes = []
    for maps in mapping_list:
        mapping_class = MappingClass()
        for map in maps:
            map_func = build_function(map)
            mapping_class.add_func(map_func)
        mapping_classes.append(mapping_class)
    
    location_list = [] 
    for seed in seed_list:
        for mapping_class in mapping_classes:
            seed = mapping_class.map(seed)
        location_list.append(seed)
        print(seed)
    print(min(location_list))

def generate_windows(seedlist: str):
    seedlist = seedlist.split(": ")[1]
    seedlist = [int(seed) for seed in seedlist.split(" ")]
    windows = []
    for i in range(0, len(seedlist), 2):
        windows.append((seedlist[i], seedlist[i+1] + seedlist[i] - 1))
    return windows

# Part 2 is mostly inspired by a comment on the advent of code subreddit, which I can't find anymore but here's the link
# https://topaz.github.io/paste/#XQAAAQBGCQAAAAAAAAA2GkofDKPu58xTyj67vWUPl6CADq35BUEbaUN3rczsMbz1HfafQMOVDEXUU5xyfgcrk5T4wiaQQYugTROug+7VPuLQK9yyiQ/X/ZE/fDCootS7zG39LSShM1QLQQHF9y24eK7TIMM3fgsR+4exCsrU3PgNHxT6S4El9qQctV2p2y/KyXfM8Tdcuowe25IFkbK2EX4REn9IbjJWVISf8bleRVpT1OHP83hjcx1RCbvl4jeOl3X4VTcvLsukWLv7b6wjku0x6aQlw0yD7dpe0YX+LRaMMZ2nMRBzMVu226na8Pwlm5W6S2e5Ogx5jIGc4pxtHt9IEFRaNLYV91uLiQiGg3UmmzWb6+Qw8h7FaRGv1OarOET0O0tCN5S5QMbNDs91WJ0Ga/jJkbb+BtbxN7p0T6feBqogRq26MqhTf9g8ywqiGBFVGYCzs1ixuOWUVEGnY5kZcl453oMLD7pfGIgJbImQ9Z509TM09RNMlScHnA8JYZw84Vy1Dn1n17CcugSGPCJ61EQu1niQNTyAMkyFGJAQG4QW21pKAkxqLdFgbCiGbMr90NarGhdoq8Ihxb6iDZhYkaIMr5WbMUlrSci1CGvP5aNRGNtQZ2ukA/g7GhZV+IWPFfo3l7gJHluXB9wBvcZAngmrrDMbIvIFc5bfJn9RKGVVc8yrhVT0s48BFs5QikAFPfZAXzuMW67/hcC+n3GQ8k8lsAUV/NxtrJA+Epwt4LNVzr2felgdht3KtmH9dYxYjqMzvmajcTyoCJsJISEUzCnrRUzP+VYRT5oNrs3JnbpVf3iN4HqsyQceteTMH6puh5hu8HnNXp0eoPHJuloh0huytGbhUkjUnNqXzB14c+iP5EuFmoO+WpwmE/1c5h6NvEFsypuKFMxAZdiXAfqC+Ce//YVP/97i1bc=
def part2():
    input = read_input()
    windows = generate_windows(input[0])
    mapping_list = split_list_at_empty(input[2:])
    mapping_list = [map[1:] for map in mapping_list]
    next_windows = []
    for map in mapping_list:
        windows.extend(next_windows)
        next_windows = []
        for map_line in map:
            new_windows = []
            map_line = map_line.split(" ")
            dst_index = int(map_line[0])
            source_start = int(map_line[1])
            source_end = source_start + int(map_line[2]) - 1
            offset = dst_index - source_start
            before = middle = after = None
            for window in windows:
                # window starts before the map
                if window[0] < source_start:
                    before = (window[0], min(source_start - 1, window[1]))
                    new_windows.append(before)
                # window ends after the map
                if window[1] > source_end:
                    after = (max(window[0], source_end + 1), window[1])
                    new_windows.append(after)
                # window and map are overlapping
                if window[0] <= source_start <= window[1] or window[0] <= source_end <= window[1] or source_start <= window[0] <= source_end or source_start <= window[1] <= source_end:
                    dst_start = max(source_start, window[0])
                    dst_end = min(source_end, window[1])
                    middle = (dst_start + offset, dst_end + offset)
                    next_windows.append(middle)
            windows = new_windows
    windows.extend(next_windows)
    
    minimum = float('inf')
    for window in windows:
        minimum = window[0] if window[0] < minimum else minimum
    print(minimum)

if __name__ == "__main__":
    part1()
    part2()
