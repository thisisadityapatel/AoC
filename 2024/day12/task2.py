import time
import collections


def get_data(filename):
    return [list(line) for line in open(filename).read().splitlines()]


def corner_exists(flags):
    if sum(flags) == 0:
        return True
    return False


def solve(grid):
    row, col = len(grid), len(grid[0])
    tracker = set()
    result = 0
    for i in range(row):
        for j in range(col):
            if (i, j) not in tracker:
                local_tracker = set()
                local_corners = 0

                def local_traverse(head, type):
                    nonlocal local_corners
                    if (
                        0 <= head[0] < row
                        and 0 <= head[1] < col
                        and grid[head[0]][head[1]] == type
                        and head not in local_tracker
                    ):
                        local_tracker.add(head)

                        # Getting the surrounding pixels
                        top = (
                            1
                            if 0 <= head[0] - 1 < row
                            and 0 <= head[1] < col
                            and grid[head[0] - 1][head[1]] == type
                            else 0
                        )
                        top_right = (
                            1
                            if 0 <= head[0] - 1 < row
                            and 0 <= head[1] + 1 < col
                            and grid[head[0] - 1][head[1] + 1] == type
                            else 0
                        )
                        right = (
                            1
                            if 0 <= head[0] < row
                            and 0 <= head[1] + 1 < col
                            and grid[head[0]][head[1] + 1] == type
                            else 0
                        )
                        bottom_right = (
                            1
                            if 0 <= head[0] + 1 < row
                            and 0 <= head[1] + 1 < col
                            and grid[head[0] + 1][head[1] + 1] == type
                            else 0
                        )
                        bottom = (
                            1
                            if 0 <= head[0] + 1 < row
                            and 0 <= head[1] < col
                            and grid[head[0] + 1][head[1]] == type
                            else 0
                        )
                        bottom_left = (
                            1
                            if 0 <= head[0] + 1 < row
                            and 0 <= head[1] - 1 < col
                            and grid[head[0] + 1][head[1] - 1] == type
                            else 0
                        )
                        left = (
                            1
                            if 0 <= head[0] < row
                            and 0 <= head[1] - 1 < col
                            and grid[head[0]][head[1] - 1] == type
                            else 0
                        )
                        top_left = (
                            1
                            if 0 <= head[0] - 1 < row
                            and 0 <= head[1] - 1 < col
                            and grid[head[0] - 1][head[1] - 1] == type
                            else 0
                        )

                        if sum([top, top_right, right]) == 0:
                            local_corners += 1
                        elif top_right == 0 and top + right == 2:
                            local_corners += 1
                        elif top_right == 1 and top + right == 0:
                            local_corners += 1

                        if sum([top, top_left, left]) == 0:
                            local_corners += 1
                        elif top_left == 0 and top + left == 2:
                            local_corners += 1
                        elif top_left == 1 and top + left == 0:
                            local_corners += 1

                        if sum([bottom, bottom_right, right]) == 0:
                            local_corners += 1
                        elif bottom_right == 0 and bottom + right == 2:
                            local_corners += 1
                        elif bottom_right == 1 and bottom + right == 0:
                            local_corners += 1

                        if sum([bottom, bottom_left, left]) == 0:
                            local_corners += 1
                        elif bottom_left == 0 and bottom + left == 2:
                            local_corners += 1
                        elif bottom_left == 1 and bottom + left == 0:
                            local_corners += 1

                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                if (
                                    abs(dj + di) == 1
                                    and 0 <= head[0] + di < row
                                    and 0 <= head[1] + dj < col
                                ):
                                    local_traverse((head[0] + di, head[1] + dj), type)

                local_traverse((i, j), grid[i][j])
                tracker = tracker.union(local_tracker)
                result += local_corners * len(local_tracker)
    return result


if __name__ == "__main__":
    start_time = time.time()
    grid = get_data("data.txt")
    output = solve(grid)
    print(output)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
