import time
import collections


def extract_data(filename):
    data = open(filename).read().splitlines()
    y_arr, x_arr = [], []
    for line in data:
        line = line.split(":")
        y = int(line[0].strip())
        x = list(map(int, line[1].strip().split(" ")))
        y_arr.append(y)
        x_arr.append(x)
    return y_arr, x_arr


def is_valid(y, x):
    queue = collections.deque()
    queue.append(x[0])
    for value in x[1:]:
        for _ in range(len(queue)):
            queue_value = queue.popleft()
            multiply_value = queue_value * value
            addition_value = queue_value + value
            if multiply_value <= y:
                queue.append(multiply_value)
            if addition_value <= y:
                queue.append(addition_value)
    return y in queue


if __name__ == "__main__":
    start_time = time.time()
    total_sum = 0
    y, x = extract_data("data.txt")

    for i in range(len(y)):
        if is_valid(y[i], x[i]):
            total_sum += y[i]

    print(total_sum)
    end_time = time.time()
    print(f"execution time:{(end_time - start_time):.6f} seconds.")
