import concurrent.futures
import time


def input_parser(filename: str):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(list(filter(lambda x: x != "", line.strip().split(" "))))
        return list(zip(*data))


def solver(data: tuple[str]):
    count = 1
    if data[-1] == "*":
        for num in data[:-1]:
            count *= int(num)
    else:
        for num in data[:-1]:
            count += int(num)
        count -= 1
    return count


def counter(data: list[tuple]) -> int:
    count = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(solver, line) for line in data]
        for future in concurrent.futures.as_completed(futures):
            try:
                count += future.result()
            except Exception as e:
                print(e)
    return count


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("data.txt")
    results = counter(data)
    end_time = time.time()
    print(results)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
