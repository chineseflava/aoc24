import math

"""Day 4 of Advent of Code 2024"""
def organize_data(data):
    """
    Split the data into rules and updates.

    OUTPUT: 
        rules (dict): dict where the value of each key is a list of numbers not allowed after key.
        updates (list): a list of updates
    """
    rules = {}
    updates = []
    next_data = False
    for item in data:
        if item == "":
            next_data = True
        elif next_data:
            update = item.split(",")
            updates.append(update)
        else:
            rule = item.split("|")
            if rules.get(rule[1]):
                rules[rule[1]] = rules.get(rule[1])+ [rule[0]]
            else:
                rules[rule[1]] = [rule[0]]

    return rules, updates

def sort_update(update, rules):
    """Sort the update according to rule."""
    sorted_update = []
    for item in update:
        if item == "61":
            a = 0
        #print(item)
        #print(update)
        if len(sorted_update) == 0:
            sorted_update += [item]
        elif rules.get(item):
            for idx, num in enumerate(sorted_update):
                if any(s in rules[item] for s in sorted_update[idx:]):
                    if idx == len(sorted_update)-1:
                        sorted_update += [item]
                        break
                else:
                    sorted_update = sorted_update[:idx] + [item] + sorted_update[idx:]
                    break
                    #print(sorted_update)
        else:
            sorted_update = [item] + sorted_update

    return sorted_update

def part1():
    with open("./input/5", 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip())
    rules, updates = organize_data(data)
    #print(f"{rules=}\n{updates=}")
    score = 0
    for update in updates:
        n = len(update)
        for idx, item in enumerate(update):
            if rules.get(item):
                
                if any(s in rules[item] for s in update[idx:]):
                    # Move to next update if the is a "not allowed number" somewhere after the current number.
                    break
                if idx == n-1:
                    points = int(update[math.floor(n/2)])
                    print(points)
                    print(update)
                    score += points
                    
    return score

def part2():  
    with open("./input/5", 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip())
    rules, updates = organize_data(data)
    failed_updates = []
    score = 0
    for update in updates:
        n = len(update)
        for idx, item in enumerate(update):
            if rules.get(item):
                if any(s in rules[item] for s in update[idx:]):
                    failed_updates.append(update)
                    break
    sorted_updates = []
    for update in failed_updates:
        sorted_updates += [sort_update(update, rules)]
    print(sorted_updates)
    for update in sorted_updates:
        n = len(update)
        points = int(update[math.floor(n/2)])
        #print(points)
        #print(update)
        score += points
                    
    return score

if __name__ == "__main__":
    #print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")