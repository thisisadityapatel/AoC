import time


def parser(filename: str):
    content = []
    with open(filename) as file:
        content = file.read().split("\n")
    return content


def solve(filename: str):
    actions = parser(filename)
    counter = 0
    position = 50
    for action in actions:
        direction, change = action[0], int(action[1:])
        if direction == "L":
            position = (position - change) % 100
        else:
            position = (position + change) % 100
        if position == 0:
            counter += 1
    return counter


if __name__ == "__main__":
    start_time = time.time()
    result = solve("data.txt")
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
