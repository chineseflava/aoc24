import bisect

def part1():
    with open("./input/1", 'r') as f:
        lines = f.readlines()
    
    left_list = []
    right_list = []
    for line in lines:
        data = line.split()
        bisect.insort(left_list, int(data[0]))
        bisect.insort(right_list, int(data[1]))
    
    answer = 0
    for left, right in zip(left_list, right_list):
        answer += abs(left-right)
    print(answer)
    return answer

def part2():
    with open("./input/1", 'r') as f:
        lines = f.readlines()
    
    left_dict = {}
    right_dict = {}
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

    print(score)

    return

if __name__ == "__main__":
    part2()