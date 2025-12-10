import itertools
import time


def input_parser(filename: str) -> list[tuple[int]]:
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(tuple(map(int, line.strip().split(","))))
    return data


def area(combination: tuple[tuple[int], tuple[int]]) -> int:
    p1, p2 = combination
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def max_area(data: list[tuple[int]]) -> int:
    tracker = 0
    combinations = list(itertools.combinations(data, 2))
    for combination in combinations:
        tracker = max(tracker, area(combination))
    return tracker


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("data.txt")
    result = max_area(data)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
