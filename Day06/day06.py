import re

def read_input():
    with open('Day06/input.txt') as f:
        lines = f.readlines()
        lines = [line.split('\n')[0] for line in lines]
        lines = [re.findall(r'\d+', line) for line in lines]
    return lines

def calc(time: int, dist: int):
  def calc_dist_from_different_hold_times(hold_time: int, total_time: int):
      result = hold_time * (total_time - hold_time)
      return result
  sum = 0   
  for i in range(1, time + 1):
      sum += 1 if calc_dist_from_different_hold_times(i, time) > dist else 0
  return sum

def part1():
    input = read_input()
    input = list(zip(input[0], input[1]))
    sum = 1
    for i in input:
        sum *= calc(int(i[0]), int(i[1]))
    print(sum)


def part2():
    input = read_input()
    l1 = l2 = ''
    for i, _ in enumerate(input[0]):
        l1 += input[0][i]
        l2 += input[1][i]
    input = (l1, l2)
    sum = calc(int(input[0]), int(input[1]))
    print(sum)

if __name__ == "__main__":
    part1()
    part2()