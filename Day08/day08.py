import re
import threading
import logging
import time
import math
from itertools import cycle

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s %(message)s",  # Define the log format
    datefmt="%Y-%m-%d %H:%M:%S",  # Define the date format for the log messages
)

def read_input():
    with open("Day08/input.txt") as f:
        lines = f.readlines()
        lines = [line.split("\n")[0] for line in lines]
    return lines


class Binary_tree:
    def __init__(self):
        self.node_map = {}

    def add_node(self, parent: str, left: str, right: str):
        self.node_map[parent] = (left, right)

    def take_step(self, node: str, direction: str):
        return self.node_map[node][0] if direction == "L" else self.node_map[node][1]


def part1():
    input = read_input()
    steps = input[0]
    tree_structure = [tree.split(" = ") for tree in input[2:]]
    bin_tree = Binary_tree()
    current_node = "AAA"
    count_steps = 0
    for tree in tree_structure:
        left, right = re.findall(r"[A-Z]{3}", tree[1])
        bin_tree.add_node(tree[0], left, right)
    while True:
        for step in steps:
            current_node = bin_tree.take_step(current_node, step)
            count_steps += 1
            if current_node == "ZZZ":
                print(count_steps)
                return 0


def thread_function(
    start_node: str,
    directions: str,
    bin_tree: Binary_tree,
    step_list: list,
    thread_id: int,
):
    current_node = start_node
    steps = 0
    while True:
        for step in directions:
            current_node = bin_tree.take_step(current_node, step)
            steps += 1
            if current_node.endswith("Z"):
                logging.info(f"{thread_id}: Found node {current_node} in {steps} steps")
                step_list[thread_id] = steps
                while True:
                    if max(step_list) > steps:
                        break
                    if end.is_set():
                        return 0


def part2_multithreading():
    # I want to use multithreading for this exercise
    # Yeah, that worked in principle but was way to slow
    logging.info("Start the script")
    global end
    end = threading.Event()
    input = read_input()
    steps = input[0]
    tree_structure = [tree.split(" = ") for tree in input[2:]]
    bin_tree = Binary_tree()
    for tree in tree_structure:
        left, right = re.findall(r"[A-Z]{3}", tree[1])
        bin_tree.add_node(tree[0], left, right)
    starting_nodes = [
        start_node[0] for start_node in tree_structure if start_node[0].endswith("A")
    ]
    step_list = [0] * len(starting_nodes)
    threads = []
    for i, start_node in enumerate(starting_nodes):
        threads.append(
            threading.Thread(
                target=thread_function,
                args=(start_node, steps, bin_tree, step_list, i),
            )
        )
    for thread in threads:
        thread.start()
    while True:
        time.sleep(0.5)
        if max(step_list) != 0 and max(step_list) == min(step_list):
            print(step_list)
            end.set()
            return 0


def part2():
    # Thougth about the cyclic directions and realized there must be a better way
    # Read about the fact that the time for XXZ to get back to XXZ is the same as 
    # the time for XXA to get to XXZ on reddit
    # Now, using Least Common Multiple is the obvious choice
    # https://en.wikipedia.org/wiki/Least_common_multiple
    input = read_input()
    steps = input[0]
    tree_structure = [tree.split(" = ") for tree in input[2:]]
    bin_tree = Binary_tree()
    starting_nodes = [
        start_node[0] for start_node in tree_structure if start_node[0].endswith("A")
    ]
    count_steps = [0] * len(starting_nodes)
    for tree in tree_structure:
        left, right = re.findall(r"[A-Z]{3}", tree[1])
        bin_tree.add_node(tree[0], left, right)
    for i, start_node in enumerate(starting_nodes):
        current_node = start_node
        for step in cycle(steps):
            current_node = bin_tree.take_step(current_node, step)
            count_steps[i] += 1
            if current_node.endswith("Z"):
                break
    print(math.lcm(*count_steps))


if __name__ == "__main__":
    part1()
    part2()
