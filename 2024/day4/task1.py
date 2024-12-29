def logic(filename) -> int:
    grid = open(filename).read().splitlines()
    word = "XMAS"
    counter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "X":
                continue
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dc == dr == 0:
                        continue
                    # check for valid range
                    if not (
                        -1 < row + 3 * dr < len(grid)
                        and -1 < col + 3 * dc < len(grid[0])
                    ):
                        continue
                    if (
                        grid[row + dr][col + dc] == "M"
                        and grid[row + 2 * dr][col + 2 * dc] == "A"
                        and grid[row + 3 * dr][col + 3 * dc] == "S"
                    ):
                        counter += 1
    return counter


if __name__ == "__main__":
    print(logic("data.txt"))
