import time
from functools import lru_cache


def parser(filename: str) -> list[str]:
    with open(filename) as file:
        content = file.read().split(",")
    return content


@lru_cache
def get_divs(n):
    return [i for i in range(n, 0, -1) if n % i == 0 and n != i]


def is_valid(number: str):
    n = len(number)
    divisors = get_divs(n)
    for div in divisors:
        new_number = number[:div] * (n // div)
        if new_number == number:
            return True
    return False


def invalid_ids(start: str, end: str) -> int:
    total = 0
    for num in range(int(start), int(end) + 1):
        if is_valid(str(num)):
            total += num
    return total


def solve(data: list[str]) -> int:
    total = 0
    for range in data:
        start, end = range.strip().split("-")
        total += invalid_ids(start, end)
    return total


if __name__ == "__main__":
    start_time = time.time()
    data = parser("data.txt")
    total = solve(data)
    end_time = time.time()
    print(total)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
