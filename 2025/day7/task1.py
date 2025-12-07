import time


def input_parser(filename: str) -> list[list[str]]:
    lines = []
    with open(filename, "r") as file:
        lines = list(map(lambda line: list(line), file.read().strip().split("\n")))
    return lines


def solver(lines: list[list[str]]):
    ray_tracker = set()
    split_count = 0
    col = len(lines[0])
    for i in range(len(lines)):
        if not ray_tracker:
            ray_tracker.add(lines[i].index("S"))
            continue
        if "^" in lines[i]:
            temp = set()
            for ray in ray_tracker:
                if lines[i][ray] == "^":
                    split_count += 1
                    if 0 <= ray - 1 < col:
                        temp.add(ray - 1)
                    if 0 <= ray + 1 < col:
                        temp.add(ray + 1)
                else:
                    temp.add(ray)
            ray_tracker = temp
    return split_count


if __name__ == "__main__":
    start_time = time.time()
    lines = input_parser("data.txt")
    result = solver(lines)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
