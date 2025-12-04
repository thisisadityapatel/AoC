import time


def input_parser(filename: str) -> list[str]:
    banks = []
    try:
        with open(filename) as file:
            banks = file.read().strip().split("\n")
    except Exception as e:
        print(e)
    return banks


def max_jolt(bank: str) -> int:
    max_left = (bank[0], 0)
    for i in range(1, len(bank) - 1):
        if bank[i] > max_left[0]:
            max_left = (bank[i], i)
    j = max_left[1] + 1
    max_right = (bank[j], j)
    for i in range(j, len(bank)):
        if bank[i] > max_right[0]:
            max_right = (bank[i], i)
    return int(max_left[0] + max_right[0])


def solve(banks: list[str]) -> int:
    total = 0
    for bank in banks:
        total += max_jolt(bank)
    return total


if __name__ == "__main__":
    start_time = time.time()
    banks = input_parser("data.txt")
    result = solve(banks)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
