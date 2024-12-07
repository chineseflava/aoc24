import re
import numpy as np

"""Day 4 of Advent of Code 2024"""

def get_all_diagonals(matrix):
    """Get diagonals."""
    diags = []
    n = len(matrix)
    mat  = np.array([list(s) for s in matrix])
    flip_mat = np.fliplr(mat)

    for i in range(n*2-1):

        # Diagonals
        diag = np.diagonal(mat, i-n+1)
        diag_str = ""
        for s in diag:
            diag_str += s
        diags.append(diag_str)

        # Anti diagonals
        anti_diag = np.diagonal(flip_mat, i-n+1)
        anti_diag_str = "".join(anti_diag)
        diags.append(anti_diag_str)
    return diags


def find_xmas(line):
    """find the sequence XMAS backwards or forwards."""
    score = 0
    pattern_template = r"XMAS"
    forward = re.findall(pattern_template,line)
    backward = re.findall(pattern_template, line[::-1])
    score = len(backward) + len(forward)
    return score

def part1():
    with open("./input/4", 'r') as f:
        lines = f.readlines()
    score = 0
    matrix = []
    for line in lines:
        matrix.append(line.strip())
    # Horizontal
    for item in matrix:
        score += find_xmas(item)
    # Vertical
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix)):
            line += matrix[j][i]
        score += find_xmas(line)
    # Diagonals
    diagonals = get_all_diagonals(matrix)
    for diag in diagonals:
        score += find_xmas(diag)
    
    return score

def if_x_mas(mat):
    """Check if 3x3-box contains an 'X-MAS'. """
    diag = "".join(np.diagonal(mat))
    anti_diag = "".join(np.diagonal(np.fliplr(mat)))
    if diag == "MAS" or diag == "SAM":
        if anti_diag == "MAS" or anti_diag =="SAM":
            return True
    return False


def part2():  
    with open("./input/4", 'r') as f:
        lines = f.readlines()
    score = 0
    data = []
    for line in lines:
        data.append(line.strip())
    n = len(data)
    matrix = np.array([list(s) for s in data])
    # 3x3 moving window
    for i in range(n-2):
        for j in range(n-2):
            sub_matrix = matrix[i:i+3,j:j+3]
            if if_x_mas(sub_matrix):
                score += 1

    return score

if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")