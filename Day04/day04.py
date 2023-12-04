def part1():
    # Read in Input
    with open('Day04/input.txt') as f:
        lines = f.readlines()
        lines = [line.split('\n')[0] for line in lines]
        lines = [line.split(': ')[1] for line in lines]
        lines = [line.split(' | ') for line in lines]
    # Preprocessing of the data
    # Each game is a list of 2 lists
    # The first list contains the winning numbers
    # The second list contains the draw numbers
    for i in range(len(lines)):
        lines[i] = [line.split(' ') for line in lines[i]]
        items_to_pop = []
        for j in range(len(lines[i][0])):
            if lines[i][0][j] == "":
                items_to_pop.append(j)
            else:
                lines[i][0][j] = int(lines[i][0][j])
        items_to_pop.reverse()
        for j in items_to_pop:
            lines[i][0].pop(j)
        items_to_pop = []
        for j in range(len(lines[i][1])):
            if lines[i][1][j] == "":
                items_to_pop.append(j)
            else:
                lines[i][1][j] = int(lines[i][1][j])
        items_to_pop.reverse()
        for j in items_to_pop:
            lines[i][1].pop(j)
    # calculate the sum of the scores
    sum = 0
    for game in lines:
        score = 0
        for number in game[1]:
            if number in game[0]:
                score += 1
        if score > 0:
            sum += 2 ** (score - 1)
    print(sum)
    

def part2():
    # Read in Input
    with open('Day04/input.txt') as f:
        lines = f.readlines()
        lines = [line.split('\n')[0] for line in lines]
        lines = [line.split(': ')[1] for line in lines]
        lines = [line.split(' | ') for line in lines]
    # Preprocessing of the data
    # Each game is a list of 2 lists
    # The first list contains the winning numbers
    # The second list contains the draw numbers
    for i in range(len(lines)):
        lines[i] = [line.split(' ') for line in lines[i]]
        items_to_pop = []
        for j in range(len(lines[i][0])):
            if lines[i][0][j] == "":
                items_to_pop.append(j)
                # lines[i][0].pop(j)
            else:
                lines[i][0][j] = int(lines[i][0][j])
        items_to_pop.reverse()
        for j in items_to_pop:
            lines[i][0].pop(j)
        items_to_pop = []
        for j in range(len(lines[i][1])):
            if lines[i][1][j] == "":
                # lines[i][1].pop(j)
                items_to_pop.append(j)
            else:
                lines[i][1][j] = int(lines[i][1][j])
        items_to_pop.reverse()
        for j in items_to_pop:
            lines[i][1].pop(j)
    card_array = [1] * len(lines)
    # calculate the amount of cards and print the sum
    for i in range(len(lines)):
        score = 0
        for number in lines[i][1]:
            if number in lines[i][0]:
                score += 1
        for j in range(i + 1, i + 1 + score):
            card_array[j] += card_array[i]
    print(sum(card_array))
        

if __name__ == "__main__":
    part1()
    part2()