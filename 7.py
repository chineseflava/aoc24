import itertools
from sympy import sympify, evalf

"""Day 7"""
def compare_combinations(item, part=1):
    numbers = item[1]
    target = int(item[0])
    if part == 2:
        operators = ["+", "*", "||"]
    else:
        operators = ["+", "*"]

    for ops in itertools.product(operators, repeat=len(numbers)-1):
        expression = numbers[0]
        result = int(numbers[0])
        for i in range(len(ops)):
            expression += ops[i] + numbers[i + 1]
            # Logics for order of operations in appearing order.
            if ops[i] == "+":
                result += int(numbers[i + 1])
            elif ops[i] == "*":
                result *= int(numbers[i + 1])
            elif ops[i] == "||":
                result = int(str(result) + numbers[i+1])
        if result == target:
            #print(target)
            return target
    return 0


def part1():
    with open("./input/7", 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        split_line = line.split(":")
        data += [[split_line[0],  split_line[1].split()]]
    #print(data)
    score = 0
    for item in data:
        score += compare_combinations(item)
    
    return score

def part2():
    with open("./input/7", 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        split_line = line.split(":")
        data += [[split_line[0],  split_line[1].split()]]
    #print(data)
    score = 0
    for item in data:
        # Add operator || into the mix...
        score += compare_combinations(item, 2)
    
    return score

if __name__ == "__main__":
    #print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")

