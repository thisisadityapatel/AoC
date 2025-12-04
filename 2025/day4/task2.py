import collections
import time


def input_parser(filename: str) -> list[list]:
    grid = []
    try:
        with open(filename) as file:
            grid = list(map(lambda grid: list(grid), file.read().strip().split("\n")))
    except Exception as e:
        print(e)
    return grid


def solve(grid: list[list]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    total = 0
    removed = set()
    stuck = collections.deque()
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "@":
                count = 0
                for dx in range(-1, 2):
                    if count > 3:
                        break
                    for dy in range(-1, 2):
                        if dx == dy and dx == 0:
                            continue
                        nx = x + dx
                        ny = y + dy
                        if (
                            -1 < nx < rows
                            and -1 < ny < cols
                            and (grid[nx][ny] == "@" or (nx, ny) in removed)
                        ):
                            count += 1
                if count < 4:
                    counter += 1
                    removed.add((x, y))
                    grid[x][y] = "."
                else:
                    stuck.append((x, y))

    while counter > 0:
        total += counter
        counter = 0
        removed = set()
        for _ in range(len(stuck)):
            x, y = stuck.popleft()
            count = 0
            for dx in range(-1, 2):
                if count > 3:
                    break
                for dy in range(-1, 2):
                    if dx == dy and dx == 0:
                        continue
                    nx = x + dx
                    ny = y + dy
                    if (
                        -1 < nx < rows
                        and -1 < ny < cols
                        and (grid[nx][ny] == "@" or (nx, ny) in removed)
                    ):
                        count += 1
            if count < 4:
                counter += 1
                removed.add((x, y))
                grid[x][y] = "."
            else:
                stuck.append((x, y))
    return total


if __name__ == "__main__":
    start_time = time.time()
    grid = input_parser("data.txt")
    result = solve(grid)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
