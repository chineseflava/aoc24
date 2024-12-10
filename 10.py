
def extract_data(input):
    """Extract the trailmap and pad edges for easier handling."""
    trail_map = []
    with open(f"./input/{input}", 'r') as f:
        lines = f.readlines()
    for line in lines:
        trail_map.append("." + line.strip() + ".")
    n = len(trail_map[0])
    trail_map = ["."*n] + trail_map + ["."*n]
    return trail_map

class Trailhead:
    """
    Class to keep track of trailheads and update them for each move.

    Args:
        start (tuple): starting position on trail_map.
        part (int): 1 for finding total endpoints for each trail start. 2 for finding totalt paths to endpoint per trail start.

    Definitions:
        move: Check if surrounding position is +1 greater in height, then update heads. Add trail if height is 9.
        add_trail: add complete trail to trails (list).
        get_score: get total amount of trails.
    
    """
    def __init__(self, start, part=1):
        
        self.start = start
        self.heads = [start]
        self.part = part
        if self.part == 2:
            self.trails = []
        else:
            self.trails = set()

    def move(self, map):
        new_heads = []
        for head in self.heads:
            x = head[1]
            y = head[0]
            height = int(map[y][x])
            next_height = str(height +1)
            if map[y+1][x] == next_height:
                new_heads.append((y+1,x))
                if map[y+1][x] == "9":
                    self.add_trail((y+1,x))
            if map[y][x+1] == next_height:
                new_heads.append((y,x+1))
                if map[y][x+1] == "9":
                    self.add_trail((y,x+1))
            if map[y-1][x] == next_height:
                new_heads.append((y-1,x))
                if map[y-1][x] == "9":
                 self.add_trail((y-1,x))
            if map[y][x-1] == next_height:   
                new_heads.append((y,x-1))
                if map[y][x-1] == "9":
                 self.add_trail((y,x-1))
        self.heads = new_heads
    def add_trail(self, trail):
        if self.part == 2:
            self.trails.append(trail)
        else:
            self.trails.add(trail)

    def get_score(self):
       return len(self.trails)

def find_trails(trail_map, part=1):
    trails = []
    for y, line in enumerate(trail_map):
        for x, num in enumerate(line):
            if num == "0":
                trails.append(Trailhead((y,x), part))
    for _ in range(9):
       for trail in trails:
          trail.move(trail_map)
    score = 0
    for trail in trails:
       score += trail.get_score()
    return score

def part1():
    trail_map= extract_data("10")
    score = find_trails(trail_map)
    return score

def part2():
    trail_map = extract_data("10")
    score = find_trails(trail_map, 2)
    return score


if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")