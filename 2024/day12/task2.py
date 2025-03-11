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
                            (head[0] - 1, head[1])
                            if 0 <= head[0] - 1 < row and 0 <= head[1] < col
                            else None
                        )
                        top_right = (
                            (head[0] - 1, head[1] + 1)
                            if 0 <= head[0] - 1 < row and 0 <= head[1] + 1 < col
                            else None
                        )
                        right = (
                            (head[0], head[1] + 1)
                            if 0 <= head[0] < row and 0 <= head[1] + 1 < col
                            else None
                        )
                        bottom_right = (
                            (head[0] + 1, head[1] + 1)
                            if 0 <= head[0] + 1 < row and 0 <= head[1] + 1 < col
                            else None
                        )
                        bottom = (
                            (head[0] + 1, head[1])
                            if 0 <= head[0] + 1 < row and 0 <= head[1] < col
                            else None
                        )
                        bottom_left = (
                            (head[0] + 1, head[1] - 1)
                            if 0 <= head[0] + 1 < row and 0 <= head[1] - 1 < col
                            else None
                        )
                        left = (
                            (head[0], head[1] - 1)
                            if 0 <= head[0] < row and 0 <= head[1] - 1 < col
                            else None
                        )
                        top_left = (
                            (head[0] - 1, head[1] - 1)
                            if 0 <= head[0] - 1 < row and 0 <= head[1] - 1 < col
                            else None
                        )

                        # checking the top right for corner
                        if top and top_right and right:
                            temp_count = sum(
                                1
                                for val in [top, top_right, right]
                                if val and grid[val[0]][val[1]] == type
                            )
                            if temp_count == 2:
                                local_corners += 1
                            elif (
                                grid[top[0]][top[1]] != type
                                and grid[right[0]][right[1]] != type
                            ):
                                local_corners += 1

                        elif not top_right and not right and not top:
                            local_corners += 1

                        # checking the top left for corner
                        if top and top_left and left:
                            temp_count = sum(
                                1
                                for val in [top, top_left, left]
                                if val and grid[val[0]][val[1]] == type
                            )
                            if temp_count == 2:
                                local_corners += 1
                            elif (
                                grid[top[0]][top[1]] != type
                                and grid[left[0]][left[1]] != type
                            ):
                                local_corners += 1

                        if not top_left and not left and not top:
                            local_corners += 1

                        # checking the bottom right for corner
                        if bottom and bottom_right and right:
                            temp_count = sum(
                                1
                                for val in [bottom, bottom_right, right]
                                if val and grid[val[0]][val[1]] == type
                            )
                            if temp_count == 2:
                                local_corners += 1
                            elif (
                                grid[bottom[0]][bottom[1]] != type
                                and grid[right[0]][right[1]] != type
                            ):
                                local_corners += 1

                        if not bottom_right and not bottom and not right:
                            local_corners += 1

                        # checking the bottom left for corner
                        if bottom and bottom_left and left:
                            temp_count = sum(
                                1
                                for val in [bottom, bottom_left, left]
                                if val and grid[val[0]][val[1]] == type
                            )
                            if temp_count == 2:
                                local_corners += 1
                            elif (
                                grid[bottom[0]][bottom[1]] != type
                                and grid[left[0]][left[1]] != type
                            ):
                                local_corners += 1

                        if not bottom and not bottom_left and not left:
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
                print(grid[i][j])
                print(local_tracker)
                print(local_corners)
                tracker = tracker.union(local_tracker)
                result += local_corners * len(local_tracker)
    return result


if __name__ == "__main__":
    start_time = time.time()
    grid = get_data("testing.txt")
    output = solve(grid)
    print(output)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
