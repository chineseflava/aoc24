import re

"""Day 3 of Advent of Code 2024"""

def find_patterns(pattern):
    """
    Function to find matches using re.

    Args: 
        pattern: to look for
    Returns (List):
        list of matches.
    """


def part1():
    with open("./input/3", 'r') as f:
        lines = f.readlines()
    score = 0
    pattern_template = r"mul\([^)\]}qwertyuiopasdfghjklzxcvbnm.;:-_*'^~¨!\"\#¤%&/]+\)"
    for line in lines:
        found_patterns = re.findall(pattern_template, line)
        #print(found_patterns)
        for pattern in found_patterns:
            numbers = pattern[4:-1].split(",")
            if len(numbers) == 2:
                score += int(numbers[0])*int(numbers[1])
    return score


def part2():
    with open("./input/3", 'r') as f:
        lines = f.readlines()
    score = 0
    pattern_template = r"mul\([^)\]}qwertyuiopasdfghjklzxcvbnm.;:-_*'^~¨!\"\#¤%&/]+\)|do\(\)|don't\(\)"
    enable = True
    for line in lines:
        found_patterns = re.findall(pattern_template, line)
        print(found_patterns)
        for pattern in found_patterns:
            if pattern == "do()":
                enable = True
            if pattern == "don't()":
                enable = False
            if enable:
                numbers = pattern[4:-1].split(",")
                if len(numbers) == 2:
                    score += int(numbers[0])*int(numbers[1])
    return score

if __name__ == "__main__":
    #print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")