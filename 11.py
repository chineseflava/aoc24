from collections import defaultdict

class Stones:
    def __init__(self, data):
        self.stones = defaultdict(int)
        for stone in data:
            self.stones[stone] = 1

    def blink(self):
        """Perform a blink and update with new stones"""
        new_stones = defaultdict(int)
        for key, val in self.stones.items():
            n = len(str(key))
            if key == 0:
                new_stones[1] += val
            elif n%2 == 0:
                new_stones[int(str(key)[:int(n/2)])] += val
                new_stones[int(str(key)[int(n/2):])] += val
            else:
                new_stones[key*2024] += val
        self.stones = new_stones

    def get_score(self, blinks):
        """Perform blinks and get score (# of stones)"""
        for i in range(blinks):
            self.blink()
        score = 0
        for key, value in self.stones.items():
            score += value
        return score

test_data = [125, 17]
data = [3, 386358, 86195, 85, 1267, 3752457, 0, 741]

def part1():
    stones = Stones(data)
    score = stones.get_score(25)
    return score

def part2():
    stones = Stones(data)
    score = stones.get_score(75)
    return score

if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")