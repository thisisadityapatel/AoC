import time
import collections


def get_data(filename):
    return [list(line) for line in open(filename).read().splitlines()]


def solve(grid):
    row, col = len(grid), len(grid[0])
    tracker = set()
    result = 0
    for i in range(row):
        for j in range(col):
            if (i, j) not in tracker:
                local_tracker = set()
                local_perimeter = 0

                def local_traverse(head, type):
                    nonlocal local_perimeter
                    if (
                        -1 < head[0] < row
                        and -1 < head[1] < col
                        and grid[head[0]][head[1]] == type
                        and head not in local_tracker
                    ):
                        local_tracker.add(head)
                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                if (abs(dj + di)) == 1:
                                    if (
                                        -1 < head[0] + di < row
                                        and -1 < head[1] + dj < col
                                    ):
                                        if grid[head[0] + di][head[1] + dj] != type:
                                            local_perimeter += 1
                                    else:
                                        local_perimeter += 1
                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                if (
                                    abs(dj + di) == 1
                                    and -1 < head[0] + di < row
                                    and -1 < head[1] + dj < col
                                ):
                                    local_traverse((head[0] + di, head[1] + dj), type)

                local_traverse((i, j), grid[i][j])
                tracker = tracker.union(local_tracker)
                result += local_perimeter * len(local_tracker)
    return result


if __name__ == "__main__":
    start_time = time.time()
    grid = get_data("data.txt")
    output = solve(grid)
    print(output)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
