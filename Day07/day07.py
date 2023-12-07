import re

def read_input():
    with open("Day07/input.txt") as f:
        lines = f.readlines()
        lines = [line.split("\n")[0] for line in lines]
        lines = [line.split(" ") for line in lines]
        for i, line in enumerate(lines):
            lines[i] = (line[0], line[1])
    return lines

def custom_sort_key(s):
    order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    return tuple(order[char] for char in s)

def custom_sort_key_p2(s):
    order = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
    return tuple(order[char] for char in s)

def eval_type_of_hand(hand: tuple, game_type: list):
    sorted_hand = sorted(hand[0])
    sorted_hand = "".join(sorted_hand)
    sorted_hand = [x.group() for x in re.finditer(r'(.)\1*', sorted_hand)]
    if len(sorted_hand) == 1:
        # 5 of a kind
        game_type[0].append(hand)
    elif len(sorted_hand) == 2:
        if max([len(x) for x in sorted_hand]) == 4:
            # 4 of a kind
            game_type[1].append(hand)
        else:
            # Full house
            game_type[2].append(hand)
    elif len(sorted_hand) == 3:
        if max([len(x) for x in sorted_hand]) == 3:
            # 3 of a kind
            game_type[3].append(hand)
        else:
            # 2 pairs
            game_type[4].append(hand)
    elif len(sorted_hand) == 4:
        # 1 pair
        game_type[5].append(hand)
    else:
        # High card
        game_type[6].append(hand)        

def eval_type_of_hand_p2(hand: tuple, game_type: list):
    sorted_hand = sorted(hand[0])
    sorted_hand = "".join(sorted_hand)
    num_Js = sorted_hand.count('J')
    sorted_hand = [x.group() for x in re.finditer(r'(.)\1*', sorted_hand)]
    if len(sorted_hand) == 1:
        # 5 of a kind
        game_type[0].append(hand)
    elif len(sorted_hand) == 2:
        if max([len(x) for x in sorted_hand]) == 4 and num_Js == 0:
            # 4 of a kind
            game_type[1].append(hand)
        elif max([len(x) for x in sorted_hand]) == 3 and num_Js == 0:
            # Full house
            game_type[2].append(hand)
        else: 
            # 5 of a kind via Js
            game_type[0].append(hand)
    elif len(sorted_hand) == 3:
        if max([len(x) for x in sorted_hand]) == 3 and num_Js == 0:
            # 3 of a kind
            game_type[3].append(hand)
        elif (max([len(x) for x in sorted_hand]) == 3 and num_Js > 0) or (max([len(x) for x in sorted_hand]) == 2 and num_Js == 2):
            # 4 of a kind
            game_type[1].append(hand)
        elif max([len(x) for x in sorted_hand]) == 2 and num_Js == 0:
            # 2 pairs
            game_type[4].append(hand)
        elif max([len(x) for x in sorted_hand]) == 2 and num_Js == 1:
            # full house
            game_type[2].append(hand)
    elif len(sorted_hand) == 4:
        if num_Js > 0:
            # 3 of a kind
            game_type[3].append(hand)
        else:
            # 1 pair
            game_type[5].append(hand)
    else:
        if num_Js > 0:
            # 1 pair
            game_type[5].append(hand)
        else:
            # High card
            game_type[6].append(hand)        


def part1():
    input = read_input()
    game_types = [[] for _ in range(7)]
    result_list = []
    for game in input:
        eval_type_of_hand(game, game_types)
    for game_type in game_types:
        game_type.sort(key = lambda x: custom_sort_key(x[0]))
        result_list.extend(game_type)
    sum = 0
    for i, game in enumerate(reversed(result_list)):
        sum += (i + 1) * int(game[1])
    print(sum)


def part2():
    input = read_input()
    game_types = [[] for _ in range(7)]
    result_list = []
    for game in input:
        eval_type_of_hand_p2(game, game_types)
    for game_type in game_types:
        game_type.sort(key = lambda x: custom_sort_key_p2(x[0]))
        result_list.extend(game_type)
    sum = 0
    for i, game in enumerate(reversed(result_list)):
        sum += (i + 1) * int(game[1])
    print(sum)


if __name__ == "__main__":
    part1()
    part2()
