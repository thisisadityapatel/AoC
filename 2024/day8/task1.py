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


def get_antonode_positions(positions, row_count, col_count):
    antinodes = set()
    for i in range(len(positions) - 1):
        for j in range(i, len(positions)):
            pos1 = positions[i]
            pos2 = positions[j]
            ant1 = (2 * pos1[0] - pos2[0], 2 * pos1[1] - pos2[1])
            ant2 = (2 * pos2[0] - pos1[0], 2 * pos2[1] - pos1[1])
            if valid_antinode(ant1, row_count, col_count) and ant1 not in positions:
                antinodes.add(ant1)
            if valid_antinode(ant2, row_count, col_count) and ant2 not in positions:
                antinodes.add(ant2)
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
