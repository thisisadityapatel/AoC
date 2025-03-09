import time


def get_map(filename):
    return [list(map(int, list(line))) for line in open(filename).read().splitlines()]


def get_trail_count(pos, map):
    row, col = len(map), len(map[0])

    def traversal(pos):
        if map[pos[0]][pos[1]] == 9:
            return 1
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i + j) == 1:
                    if (
                        -1 < pos[0] + i < row
                        and -1 < pos[1] + j < col
                        and map[pos[0] + i][pos[1] + j] - map[pos[0]][pos[1]] == 1
                    ):
                        count += traversal((pos[0] + i, pos[1] + j))
        return count

    return traversal(pos)


if __name__ == "__main__":
    start_time = time.time()
    map = get_map("data.txt")
    starting_points = set()
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 0:
                starting_points.add((i, j))

    trail_count = 0
    for start in starting_points:
        trail_count += get_trail_count(start, map)

    print(trail_count)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
