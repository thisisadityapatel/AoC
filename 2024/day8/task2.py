import time
import collections


def get_grid(filename):
    return [list(line) for line in open(filename).read().splitlines()]


def get_character_positions(grid):
    positions = collections.defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                positions[grid[i][j]].append((i, j))
    return positions


def valid_antinode(position, row_count, col_count):
    if 0 <= position[0] < row_count and 0 <= position[1] < col_count:
        return True
    return False


def is_in_line(pos1, pos2, point):
    (x1, y1) = pos1
    (x2, y2) = pos2
    (x3, y3) = point
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0


def get_antonode_positions(positions, row_count, col_count):
    antinodes = set()
    for pi in range(len(positions) - 1):
        for pj in range(pi + 1, len(positions)):
            pos1 = positions[pi]
            pos2 = positions[pj]
            for i in range(row_count):
                for j in range(col_count):
                    if pos1[1] == pos2[1]:
                        if i <= pos1[0] or i >= pos2[0]:
                            if is_in_line(pos1, pos2, (i, j)):
                                antinodes.add((i, j))
                    else:
                        if j <= pos1[1] or j >= pos2[1]:
                            if is_in_line(pos1, pos2, (i, j)):
                                antinodes.add((i, j))
    return antinodes


if __name__ == "__main__":
    start_time = time.time()
    grid = get_grid("data.txt")
    positions = get_character_positions(grid)
    antinodes = set()
    row_count = len(grid)
    col_count = len(grid[0])
    for key, value in positions.items():
        antinodes = antinodes.union(get_antonode_positions(value, row_count, col_count))
    print(len(antinodes))
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
