import bisect

"""Day 1 of Advent of Code 2024"""
def part1():
    with open("./input/1", 'r') as f:
        lines = f.readlines()
    
    left_list = []
    right_list = []
    # extract left and right number and put into sorted list.
    for line in lines:
        data = line.split()
        bisect.insort(left_list, int(data[0]))
        bisect.insort(right_list, int(data[1]))
    
    score = 0
    for left, right in zip(left_list, right_list):
        score += abs(left-right)
    
    return score

def part2():
    with open("./input/1", 'r') as f:
        lines = f.readlines()
    
    left_dict = {}
    right_dict = {}

    # Put values into dicts to keep track of appearances.
    for line in lines:
        data = line.split()
        if data[0] in left_dict:
            left_dict[data[0]] += 1
        else:
            left_dict[data[0]] = 1

        if data[1] in right_dict:
            right_dict[data[1]] += 1
        else:
            right_dict[data[1]] = 1

    score = 0

    for key in left_dict:
        if key in right_dict:
            data = int(key) * left_dict[key] * right_dict[key]
            score += data

    return score

if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 1: {part2()}")
    