# optimizations using mutation algorithm for caching and also a mathematical approach for calculating the length of the string.

import time
import collections
import math

def get_data(filename):
    return list(map(int, open(filename).read().split()))

def solve(nums):
    tracker = collections.Counter(nums)

    def mutate(num):
        if num == 0:
            return [1]
        digit_length  = int(math.log10(num)) + 1
        if digit_length % 2 == 0:
            divisor = 10 ** (digit_length // 2)
            return [num % divisor, num // divisor]
        return [num * 2024]

    for _ in range(75):
        new_tracker = collections.defaultdict(int)
        for num, count in tracker.items():
            for subnum in mutate(num):
                new_tracker[subnum] += count
        tracker = new_tracker
    return sum(tracker.values())

if __name__ == "__main__":
    start_time = time.time()
    nums = get_data('data.txt')
    output = solve(nums)
    print(output)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
