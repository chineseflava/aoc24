from collections import deque
import math

def extract_data(input):
    
    with open(f"./input/{input}", 'r') as f:
        lines = f.readlines()
    data = lines[0]
    return data

def get_disk_map(data):
    disk_map = []
    for idx, num in enumerate(data):
        if idx%2 == 1:
            disk_map += "."*int(num)
        if idx%2 == 0:
            disk_map += [math.floor(idx/2)]*int(num)
    #print(disk_map)
    return disk_map

def sort_data(map):
    n = len(map)
    #print("Sorted Map: " + "".join(map))
    for idx in range(n):
        s = map[-idx-1]
        if s != ".":
            pos1 = -idx-1
            for jdx, num in enumerate(map):
                if num == ".":
                    pos2 = jdx
                    break
            temp = map[pos1]
            map[pos1] = map[pos2]
            map[pos2] = temp
        #print("Sorted Map: " + "".join(map))
    sorted_map = []
    for idx, num in enumerate(map):
        if num != ".":
            print(num)
            sorted_map.append(num)

    return sorted_map


def get_score(data):
    score = 0
    for idx, num in enumerate(data):
        score += idx * num
    return score

def part1():
    data= extract_data("9")
    
    disk_map = get_disk_map(data)
    sorted_data = sort_data(disk_map)
    score = get_score(sorted_data)

    return score

def part2():
    data = extract_data("8")

        
    score = 0
    return score


if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    #print(f"Answer part 2: {part2()}")