import numpy as np

class Guard:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        self.init_pos = pos
        self.outside = False
    def rotate_right(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"  
    def rotate_left(self):
        if self.direction == "^":
            self.direction = "<"
        elif self.direction == ">":
            self.direction = "^"
        elif self.direction == "v":
            self.direction = ">"
        elif self.direction == "<":
            self.direction = "v"  

    def set_pos(self, new_pos):
        self.pos = new_pos



class GuardMap:
    def __init__(self, matrix, obstacles, guard):
        self.matrix = matrix
        self.obstacles = obstacles
        self.guard = guard

    def step_forward(self):
        pos = self.guard.pos
        direction = self.guard.direction
        self.matrix[pos[0]][pos[1]] = 1
        #Check position in front of guard
        next_pos = ()
        if direction == "^":
            next_pos = (pos[0]-1, pos[1])
        if direction == ">":
            next_pos = (pos[0], pos[1]+1)
        if direction == "v":
            next_pos = (pos[0]+1, pos[1])
        if direction == "<":
            next_pos = (pos[0], pos[1]-1)
        #If obstacles or edge, rotate
        n = len(self.matrix)
        #If obstacles or outside matrix, rotate
        if next_pos in self.obstacles:
            self.guard.rotate_right()
                # If next_pos is outside of matrix, guard is out.
        elif next_pos[0]>=n or next_pos[1]>=n or next_pos[0]*next_pos[1]<0:
            self.guard.outside = True
        #if not, move guard to this position
        else:
            self.guard.set_pos(next_pos)

    def step_backward(self):
        pos = self.guard.pos
        direction = self.guard.direction
        self.matrix[pos[0]][pos[1]] = 1
        #Check position in front of guard
        next_pos = ()
        if direction == "^":
            next_pos = (pos[0]+1, pos[1])
        if direction == ">":
            next_pos = (pos[0], pos[1]-1)
        if direction == "v":
            next_pos = (pos[0]-1, pos[1])
        if direction == "<":
            next_pos = (pos[0], pos[1]+1)
        #If obstacles or edge, rotate
        n = len(self.matrix)
        #If obstacles or outside matrix, rotate
        if next_pos in self.obstacles:
            self.guard.rotate_left()
        # If next_pos is outside of matrix, guard is out.
        elif next_pos[0]>=n or next_pos[1]>=n or next_pos[0]*next_pos[1]<0:
            self.guard.outside = True
        #if not, move guard to this position
        else:
            self.guard.set_pos(next_pos)

    def get_score(self):
        score = 0
        for item in self.matrix:
            for num in item:
                score += num
        return score

def handle_data(data):
    n = len(data)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    obstacles = set()
    guard = None
    for y in range(n):
        for x in range(n):
            if data[y][x]=="#":
                obstacles.add((y,x))
            elif data[y][x] != ".":
                guard = Guard((y,x), data[y][x])
    return matrix, obstacles, guard


def part1():
    with open("./input/6", 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip("\n"))
    print(data)

    matrix, obstacles, guard = handle_data(data)
    guard_map = GuardMap(matrix, obstacles, guard)


    while not guard_map.guard.outside:
        guard_map.step_forward()
        print(guard_map.guard.pos)
    
    score = guard_map.get_score()

    return score

if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    #print(f"Answer part 2: {part2()}")