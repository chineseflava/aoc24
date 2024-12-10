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

def get_disk_map2(data):
    disk_map = []
    space_log = deque()
    disk_log = deque()
    log_idx = 0
    for idx, num in enumerate(data):
        if idx%2 == 1:
            disk_map += "."*int(num)
            space_log.append({"idx": log_idx, "len": int(num)})
            log_idx += int(num)
        if idx%2 == 0:
            id = math.floor(idx/2)
            disk_map += [id]*int(num)
            disk_log.append({"idx": log_idx, "len": int(num), "id": id})
            log_idx += int(num)
    #print(disk_map)
    return disk_map, space_log, disk_log

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
            #print(num)
            sorted_map.append(num)

    return sorted_map


def sort_data2(disk_map, disk_log, space_log):
    
    while disk_log:
        next_disk = disk_log.pop()
        n = next_disk["len"]
        space = ["."]*n

        idx = next((i for i in range(len(disk_map) - len(space)- +1) if disk_map[i:i+len(space)]==space), None)
        
        if idx:
            if idx < next_disk["idx"]:
                pos1 = idx
                pos2 = next_disk["idx"]
                temp = disk_map[pos1:pos1+n]
                disk_map[pos1:pos1+n] = disk_map[pos2:pos2+n]
                disk_map[pos2:pos2+n] = temp
                #print(disk_map)
    return disk_map

def get_score(data):
    score = 0
    for idx, num in enumerate(data):
        if num != ".":
            score += idx * num
    return score

def part1():
    data= extract_data("9")
    
    disk_map = get_disk_map(data)
    sorted_data = sort_data(disk_map)
    score = get_score(sorted_data)

    return score

def part2():
    data = extract_data("9")
    disk_map, space_log, disk_log = get_disk_map2(data)
    #print(space_log, disk_log)
    sorted_data = sort_data2(disk_map, disk_log, space_log)    
    score = get_score(sorted_data)
    return score


if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")