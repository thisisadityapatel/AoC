import time


def input_parser(filename: str) -> list[list[str]]:
    lines = []
    with open(filename, "r") as file:
        lines = list(map(lambda line: list(line), file.read().strip().split("\n")))
    return lines


def solver(lines: list[list[str]]) -> int:
    rows = len(lines)
    cols = len(lines[0])
    mem = {}

    def dfs(x, y):
        if y == rows:
            return 1
        if (x, y) in mem:
            return mem[(x, y)]
        total = 0
        if lines[y][x] != "^":
            total += dfs(x, y + 1)
        else:
            if 0 <= x + 1 < cols:
                total += dfs(x + 1, y + 1)
            if 0 <= x - 1 < cols:
                total += dfs(x - 1, y + 1)
        mem[(x, y)] = total
        return total

    return dfs(lines[0].index("S"), 1)


if __name__ == "__main__":
    start_time = time.time()
    lines = input_parser("data.txt")
    result = solver(lines)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
