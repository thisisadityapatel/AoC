import time


def parser(filename: str) -> list[str]:
    with open(filename) as file:
        content = file.read().split(",")
    return content


def invalid_ids(start: str, end: str) -> int:
    start_len = len(start)
    end_len = len(end)
    if start_len == end_len and start_len % 2 != 0:
        return 0
    if start_len < end_len:
        if start_len % 2 == 0:
            end = "9" * start_len
        else:
            start = "1" + ("0" * start_len)
    mid = len(start) // 2
    left_start = int(start[:mid])
    left_end = int(end[:mid])
    total = 0
    for num in range(left_start, left_end + 1):
        num = int(str(num) + str(num))
        if int(start) <= num <= int(end):
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
