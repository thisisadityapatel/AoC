import time
from collections import deque


def input_parser(filename: str):
    points = []
    with open(filename, "r") as file:
        for line in file:
            points.append(tuple(map(int, line.strip().split(","))))
    return points


def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    if dx > dy:
        err = dx / 2
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points.append((x2, y2))
    return points


def fill_polygon(points):
    # close polygon
    pts = points + [points[0]]

    # find bounds
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 3
    height = max_y - min_y + 3

    # grid indexed as grid[y][x]
    grid = [["." for _ in range(width)] for _ in range(height)]

    # draw edges
    for i in range(len(points)):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        line = bresenham_line(
            x1 - min_x + 1, y1 - min_y + 1, x2 - min_x + 1, y2 - min_y + 1
        )
        for x, y in line:
            grid[y][x] = "#"

    # flood-fill from outside
    q = deque([(0, 0)])
    outside = set([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == "." and (nx, ny) not in outside:
                    outside.add((nx, ny))
                    q.append((nx, ny))

    # fill interior
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "." and (x, y) not in outside:
                grid[y][x] = "#"

    return grid, min_x, min_y


def get_border(grid):
    h, w = len(grid), len(grid[0])
    borders = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < w and 0 <= ny < h) or grid[ny][nx] == ".":
                        borders.add((x, y))
                        break

    return borders


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("test.txt")
    end_time = time.time()
    grid, bx, by = fill_polygon(data)
    border = get_border(grid)

    # print result
    for y, row in enumerate(grid):
        print("".join(row))
    print(f"Execution time: {end_time - start_time:.6f} seconds")


# y=8
# y=7     	 	.	.	.	.	.	#	.	.	.	#
# y=6     	 	.	.	.	.	.	.	.	.	.	.
# y=5     	 	#	.	.	.	.	#	.	.	.	.
# y=4     	 	.	.	.	.	.	.	.	.	.	.
# y=3     	 	#	.	.	.	.	.	.	#	.	.
# y=2     	 	.	.	.	.	.	.	.	.	.	.
# y=1     	 	.	.	.	.	.	.	.	#	.	#
# y=0
#        0	1	2	3	4	5	6	7	8	9	10	11	12	13
