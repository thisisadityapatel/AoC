grid = open("data.txt").read().splitlines()
counter = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if not grid[row][col] == "A":
            continue
        # checking for the first diagonal
        store = ["M", "S"]
        for dr, dc in [(-1, -1), (1, 1)]:
            if not (-1 < row + dr < len(grid) and -1 < col + dc < len(grid[0])):
                continue
            if grid[row + dr][col + dc] in store:
                store.remove(grid[row + dr][col + dc])
        if store:
            continue

        # checking for the second diagonal
        store = ["M", "S"]
        for dr, dc in [(-1, 1), (1, -1)]:
            if not (-1 < row + dr < len(grid) and -1 < col + dc < len(grid[0])):
                continue
            if grid[row + dr][col + dc] in store:
                store.remove(grid[row + dr][col + dc])
        if store:
            continue

        counter += 1

print(counter)
