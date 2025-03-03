import time

start_time = time.time()
grid = open("data.txt").read().splitlines()
positions = []
direction = 0
mapping = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # format: (row, col)

head = None

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "^":
            head = (row, col)
            positions.append(head)
            break
    if len(positions) == 1:
        break

while 0 < head[0] < len(grid) - 1 and 0 < head[1] < len(grid[0]) - 1:
    if grid[head[0] + mapping[direction][0]][head[1] + mapping[direction][1]] == "#":
        direction = (direction + 1) % 4
    head = (head[0] + mapping[direction][0], head[1] + mapping[direction][1])
    positions.append(head)

end_time = time.time()
print(len(set(positions)))
print(f"execution time: {end_time - start_time:.6f} seconds")
