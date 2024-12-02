"""Day 1 of Advent of Code 2024"""

def safe_data(data)->bool:
    """Function to check if data is safe."""
    safe = True
    if data == sorted(data) or data == sorted(data, reverse=True):
        for j in range(1,len(data)):
            diff = abs(data[j]-data[j-1])
            if diff > 3 or diff == 0:
                safe = False
    else:
        safe = False

    return safe

def part1():
    with open("./input/2", 'r') as f:
        lines = f.readlines()

    score = 0

    for i in range(len(lines)):
        data = [int(s) for s in lines[i].split()]
        safe = safe_data(data)
        if safe == True:
            score += 1     
    
    return score

def part2():
    with open("./input/2", 'r') as f:
        lines = f.readlines()

    score = 0

    for i in range(len(lines)):
        data = [int(s) for s in lines[i].split()]
        # Check every possible vector with one value removed to see if safe.
        for k in range(len(data)):
            partial_data = data[:k] + data[k+1:]
            safe = safe_data(partial_data)
            if safe == True:
                score +=1
                break      
    
    return score

if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")