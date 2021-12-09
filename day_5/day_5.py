from itertools import chain 

def load_data():
    with open("input", "r") as f:
        data = f.read().splitlines()
        coordinates = [line.split(' -> ') for line in data]
        coordinates = [line[0].split(',') + line[1].split(',') for line in coordinates]
        return [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in coordinates]

def create_grid():
    return [[0 for x in range(1000)] for y in range(1000)]

def mark_h_v_lines(coordinates, grid):
    for x1, y1, x2, y2 in coordinates:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] += 1
    return grid
            
def count_grid_points(grid):
    return len([x for x in chain.from_iterable(grid) if x > 1])

def part_1(coordinates):
    grid = mark_h_v_lines(coordinates, create_grid())
    return count_grid_points(grid)

print(f'Part 1: {part_1(load_data())}')     

def mark_lines(coordinates, grid):
    for x1, y1, x2, y2 in coordinates:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] += 1
        else:
            x_step = 1 if x1 < x2 else -1
            y_step = 1 if y1 < y2 else -1
            for x in range(x1, x2 + x_step, x_step):
                grid[x][y1] += 1
                y1 += y_step
    return grid

def part_2(coordinates):
    grid = mark_lines(coordinates, create_grid())
    return count_grid_points(grid)

print(f'Part 2: {part_2(load_data())}')     