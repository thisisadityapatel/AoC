import time
import math
import collections


def get_data(filename):
    return list(map(int, open(filename).read().split()))


def solve(nums, blinks):
    stones = collections.Counter(nums)

    def mutate(stone):
        if stone == 0:
            return [1]
        digits = str(stone)
        half, remainder = divmod(len(digits), 2)
        if remainder == 0:
            return map(int, (digits[:half], digits[half:]))
        return [stone * 2024]

    for _ in range(blinks):
        new_stones = collections.defaultdict(int)
        for stone, count in stones.items():
            for child in mutate(stone):
                new_stones[child] += count
        stones = new_stones
    return sum(stones.values())


if __name__ == "__main__":
    start_time = time.time()
    data = get_data("data.txt")
    result = solve(data, 75)
    print(result)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.06f} seconds")
