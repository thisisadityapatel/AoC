import time


def input_parser(filename: str):
    ranges = []
    ids = []
    with open(filename, "r") as file:
        data = file.read().strip().split("\n")
        split_index = data.index("")
        ranges = list(
            map(lambda range: list(map(int, range.split("-"))), data[:split_index])
        )
        ids = list(map(int, data[split_index + 1 :]))
    return ranges, ids


def resolve_range(ranges: list[list]) -> list[list]:
    ranges.sort(key=lambda x: x[0])
    stack = []
    for range in ranges:
        if not stack:
            stack.append(range)
            continue
        curr_start, curr_end = range
        prev_start, prev_end = stack.pop()
        if curr_start > prev_end:
            stack.append([prev_start, prev_end])
            stack.append([curr_start, curr_end])
        else:
            stack.append([prev_start, max(curr_end, prev_end)])
    return stack


def counter(ranges: list[list], ids: list[int]) -> int:
    ids.sort()
    i = 0
    count = 0
    for id in ids:
        while i < len(ranges):
            if ranges[i][0] <= id <= ranges[i][1]:
                count += 1
                break
            if ranges[i][0] > id:
                break
            if ranges[i][1] < id:
                i += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    ranges, ids = input_parser("data.txt")
    ranges = resolve_range(ranges)
    count = counter(ranges, ids)
    print(count)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
