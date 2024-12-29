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

while 0 < head[0] < len(grid) - 1 and 0 < head[1] < len(grid[0]) - 1:
    if grid[head[0] + mapping[direction][0]][head[1] + mapping[direction][1]] == "#":
        direction = (direction + 1) % 4
    head = (head[0] + mapping[direction][0], head[1] + mapping[direction][1])
    positions.append(head)

print(len(set(positions)))
