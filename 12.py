
def extract_data(input):
    """Extract"""
    garden_map = []
    with open(f"./input/{input}", 'r') as f:
        lines = f.readlines()
    for line in lines:
        garden_map.append(line.strip())
    return garden_map

def get_clusters(matrix):
    """Using a Depth-First search method."""
    clusters = {}
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    def dfs(i,j,cluster):
        visited[i][j] = True
        cluster.append((i,j))
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                if not visited[ni][nj] and matrix[ni][nj] == matrix[i][j]:
                    dfs(ni, nj, cluster)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited[i][j]:
                cluster = []
                dfs(i,j,cluster)
                value = matrix[i][j]
                if value not in clusters:
                    clusters[value] = []
                clusters[value].append(cluster)
    return clusters

def get_region_cost(region):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    fences = 0
    region_size = len(region)
    for coord in region:
        #print(coord)
        for di, dj in directions:
            prox_coord = (coord[0] + di, coord[1] + dj)
            if prox_coord not in region:
                fences += 1
    return fences * region_size

def get_bulk_region_cost(region, matrix):
    """Use a Moore-Neighbor tracing algorithm to find boundaries?"""
    region_size = len(region)

    # Amount of corners should be equal to sides. 
    def find_corners(region):
        outer_corners = []
        inner_corners = []
        for item in region:
            i, j = item[0], item[1]
            N = (i-1,j)
            NW = (i-1,j-1)
            W = (i,j-1)
            SW = (i+1,j-1)
            S = (i+1,j)
            SE = (i+1,j+1)
            E = (i, j+1)
            NE = (i-1, j+1)
            if N not in region and NW not in region and W not in region:
                outer_corners.append(NW)
            if S not in region and SW not in region and W not in region:
                outer_corners.append(SW)
            if S not in region and SE not in region and E not in region:
                outer_corners.append(SE)
            if N not in region and NE not in region and E not in region:
                outer_corners.append(NE)
            if N in region and E in region and (NE not in region):
                inner_corners.append(item)
            if S in region and E in region and (SE not in region):
                inner_corners.append(item)
            if S in region and W in region and (SW not in region):
                inner_corners.append(item)
            if N in region and W in region and (NW not in region):
                inner_corners.append(item)
        return len(outer_corners) + len(inner_corners)

    corners = find_corners(region)

    return corners* region_size

    

def part1():
    garden_map = extract_data("12")
    regions = get_clusters(garden_map)
    score = 0
    for region_type in regions:
        for region in regions[region_type]:
            cost = get_region_cost(region)
            score += cost
    
    return score

def part2():
    garden_map = extract_data("12")
    regions = get_clusters(garden_map)
    score = 0
    for region_type in regions:
        for region in regions[region_type]:
            cost = get_bulk_region_cost(region, garden_map)
            score += cost
    
    return score

if __name__ == "__main__":
    print(f"Answer part 1: {part1()}")
    print(f"Answer part 2: {part2()}")