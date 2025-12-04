import time


def input_parser(filename: str) -> list[str]:
    grid = []
    try:
        with open(filename) as file:
            grid = file.read().strip().split("\n")
    except Exception as e:
        print(e)
    return grid


def solve(grid: list[str]):
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
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
                        if -1 < nx < rows and -1 < ny < cols and (grid[nx][ny] == "@"):
                            count += 1
                if count < 4:
                    counter += 1
    return counter


if __name__ == "__main__":
    start_time = time.time()
    grid = input_parser("data.txt")
    result = solve(grid)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
