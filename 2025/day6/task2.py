import concurrent.futures
import math
import time


def input_parser(filename: str):
    lines = []
    collection = []
    digits = []

    with open(filename, "r") as file:
        for line in file:
            lines.append(line[:-1])

    data = lines[:-1]
    operations = lines[-1] + " "
    for i in range(len(operations) - 1, -1, -1):
        number = ""
        for line in data:
            if line[i] != " ":
                number += line[i]
        if number:
            digits.append(int(number))
        if operations[i] in ["+", "*"]:
            collection.append((digits, operations[i]))
            digits = []
            i -= 1
    return collection


def solver(data: tuple):
    if data[1] == "+":
        return sum(data[0])
    return math.prod(data[0])


def counter(data: list) -> int:
    count = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(solver, unit) for unit in data]
        for future in concurrent.futures.as_completed(futures):
            try:
                count += future.result()
            except Exception as e:
                print(e)
    return count


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("data.txt")
    result = counter(data)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
