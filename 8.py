import itertools

def extract_data(input):
    antennas = {}
    
    with open(f"./input/{input}", 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip())
    n = len(data)
    for y, line in enumerate(data):
        for x, item in enumerate(line):
            if item != ".":
                if antennas.get(item):
                    antennas[item] += [(y,x)]
                else:
                    antennas[item] = [(y,x)]
    #print(antennas)
    return antennas, n

def part1():
    antennas, n = extract_data("8")
    anodes = set()
    for freq in antennas:
        combinations = list(itertools.combinations(antennas[freq], 2))
        for combo in combinations:
            a1 = combo[0]
            a2 = combo[1]
            dy = a1[0]-a2[0]
            dx = a1[1]-a2[1]
            anode1 = (a1[0]+dy, a1[1]+dx)
            anode2 = (a2[0]-dy, a2[1]-dx)
            if anode1[0] >= 0 and anode1[0]<n and anode1[1] >= 0 and anode1[1]<n:
                anodes.add(anode1)
            if anode2[0] >= 0 and anode2[0]<n and anode2[1] >= 0 and anode2[1]<n:
                anodes.add(anode2)
    #print(f"{anodes=}")
    score = len(anodes)
    return score

def part2():
    antennas, n = extract_data("8")
    anodes = set()
    for freq in antennas:
        combinations = list(itertools.combinations(antennas[freq], 2))
        for combo in combinations:
            a1 = combo[0]
            a2 = combo[1]
            anodes.add(a1)
            anodes.add(a2)
            dy = a1[0]-a2[0]
            dx = a1[1]-a2[1]
            anode1 = (a1[0]+dy, a1[1]+dx)
            while anode1[0] >= 0 and anode1[0]<n and anode1[1] >= 0 and anode1[1]<n:
                anodes.add(anode1)
                anode1 = anode1[0]+dy, anode1[1]+dx


            anode2 = (a2[0]-dy, a2[1]-dx)
            while anode2[0] >= 0 and anode2[0]<n and anode2[1] >= 0 and anode2[1]<n:
                anodes.add(anode2)
                anode2 = (anode2[0]-dy, anode2[1]-dx)
    print(f"{anodes=}")
    matrix = ["."*n]*n
    for anode in anodes:
        y = anode[0]
        x = anode[1]
        matrix[y] = matrix[y][:x] + "#" + matrix[y][x+1:]
    for line in matrix:
        print(line)
        
    score = len(anodes)
    return score

if __name__ == "__main__":
    #print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")