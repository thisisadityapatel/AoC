# using backtracking recursion algorithm for counting the number of possible solutions

import time
import re
import collections

button_regex = r"X\+(\d+), Y\+(\d+)"
prize_regex = r"X=(\d+), Y=(\d+)"


def get_combinations(target, nums):
    dp = collections.defaultdict(list)
    dp[0] = [[]]  # Base case: One way to make sum 0 (empty set)

    for num in nums:
        for current_sum in range(num, target + 1):
            for prev_comb in dp[current_sum - num]:
                dp[current_sum].append(prev_comb + [num])  # Add new valid combinations

    return [tuple(collections.Counter(val).values()) for val in dp[target]]


def get_data(filename):
    # data format return [[(X,Y) of button A, (X, Y) of button B, (X, Y) of prize], ...]
    data = open(filename).read().splitlines()
    collection = []
    for i in range(0, len(data), 4):
        match = re.search(button_regex, data[i])
        if match:
            button_a_x_value = int(match.group(1))
            button_a_y_value = int(match.group(2))
        match = re.search(button_regex, data[i + 1])
        if match:
            button_b_x_value = int(match.group(1))
            button_b_y_value = int(match.group(2))
        match = re.search(prize_regex, data[i + 2])
        if match:
            prize_x_value = int(match.group(1))
            prize_y_value = int(match.group(2))

        collection.append(
            [
                (button_a_x_value, button_a_y_value),
                (button_b_x_value, button_b_y_value),
                (prize_x_value, prize_y_value),
            ]
        )
    return collection


def solve(data):
    count = 0
    for data_point in data:
        a_b_x_combinations = set(
            get_combinations(data_point[2][0], [data_point[0][0], data_point[1][0]])
        )
        a_b_y_combinations = set(
            get_combinations(data_point[2][1], [data_point[0][1], data_point[1][1]])
        )
        intersection = set.intersection(a_b_x_combinations, a_b_y_combinations)
        if intersection:
            print(intersection)
            min_tuple = min(intersection, key=lambda x: x[0])
            count += min_tuple[0] * 3 + min_tuple[1]
    return count


if __name__ == "__main__":
    start_time = time.time()
    data = get_data("data.txt")
    result = solve(data)
    print(result)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
