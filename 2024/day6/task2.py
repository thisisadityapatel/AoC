import time

mapping = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # format: (row, col)


def has_cycle(gridmap):
    positions = set()
    direction = 0
    head = None
    row_length = len(gridmap)
    col_length = len(gridmap[0])

    for row in range(row_length):
        for col in range(col_length):
            if gridmap[row][col] == "^":
                head = (row, col)
                positions.add((head[0], head[1], direction))
                break
        if head:
            break

    if not head:
        return False

    while 0 < head[0] < row_length - 1 and 0 < head[1] < col_length - 1:
        if (
            gridmap[head[0] + mapping[direction][0]][head[1] + mapping[direction][1]]
            == "#"
        ):
            direction = (direction + 1) % 4
        head = (head[0] + mapping[direction][0], head[1] + mapping[direction][1])
        if (head[0], head[1], direction) in positions:
            return True
        positions.add((head[0], head[1], direction))
    return False


def get_path_positions(gridmap):
    positions = set()
    direction = 0
    head = None
    row_length = len(gridmap)
    col_length = len(gridmap[0])

    for row in range(len(gridmap)):
        for col in range(len(gridmap[0])):
            if gridmap[row][col] == "^":
                head = (row, col)
                positions.add(head)
                break
        if head:
            break

    while 0 < head[0] < row_length - 1 and 0 < head[1] < col_length - 1:
        if (
            gridmap[head[0] + mapping[direction][0]][head[1] + mapping[direction][1]]
            == "#"
        ):
            direction = (direction + 1) % 4
        head = (head[0] + mapping[direction][0], head[1] + mapping[direction][1])
        positions.add(head)
    return positions


def print_grid(gridmap):
    for line in gridmap:
        print("".join(line))
    print()


if __name__ == "__main__":
    start_time = time.time()
    grid = [list(line) for line in open("data.txt").read().splitlines()]
    positions = get_path_positions(gridmap=grid)
    count = 0
    for pos in positions:
        initial_value = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = "#"
        if has_cycle(gridmap=grid):
            count += 1
        grid[pos[0]][pos[1]] = initial_value
    end_time = time.time()
    print(count)
    print(f"execution time: {end_time - start_time:.6f} seconds")
