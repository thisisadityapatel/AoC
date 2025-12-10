import itertools
import time


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
    return set(points)


def get_all_edges(points):
    pts = points + [points[0]]
    edges = set()
    for i in range(len(points)):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        edge_line = bresenham_line(x1, y1, x2, y2)
        edges = edges.union(edge_line)
    return edges


def diagonal_red_tile_positions(points):
    combinations = itertools.combinations(points, 2)
    return list(
        filter(
            lambda combination: not (
                combination[0][0] == combination[1][0]
                or combination[0][1] == combination[1][1]
            ),
            combinations,
        )
    )


def solver(combinations, edges) -> int:
    max_area = 0
    for combination in combinations:
        p1, p2 = combination
        x1, y1 = p1
        x2, y2 = p2
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        current_area = width * height
        flag = True
        for edge in edges:
            if (xmin < edge[0] < xmax) and (ymin < edge[1] < ymax):
                flag = False
                break
        if flag:
            max_area = max(current_area, max_area)
    return max_area


if __name__ == "__main__":
    start_time = time.time()
    points = input_parser("data.txt")
    edges = get_all_edges(points)
    combinations = diagonal_red_tile_positions(points)
    result = solver(combinations, edges)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
