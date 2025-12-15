import collections
import time


def input_parser(filename: str) -> list[tuple[int]]:
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(tuple(line.strip().split(" ")))
    return data


def transform(data):
    new_data = []
    for point in data:
        # capture the desired light bulb states.
        odd_number_lights = set(
            [i for i, value in enumerate(point[0][1:-1]) if value == "#"]
        )

        # capture buttons available.
        buttons = []
        for button_text in point[1:-1]:
            buttons.append(frozenset(map(int, button_text[1:-1].split(","))))
        new_data.append([odd_number_lights, buttons])
    return new_data


def find_min(point):
    target, buttons = point
    visited = {frozenset()}
    queue = collections.deque(
        [(frozenset(), None, 0)]
    )  # (current_state, prev_button, steps)

    # BFS
    while queue:
        current, prev_btn, steps = queue.popleft()
        if current == target:
            return steps
        for button in buttons:
            if button == prev_btn:
                continue

            new_state = frozenset(current.symmetric_difference(button))

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, button, steps + 1))

    return float("inf")  # no solution.


def counter(data):
    count = 0
    for point in data:
        count += find_min(point)
    return count


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("data.txt")
    data = transform(data)
    count = counter(data)
    end_time = time.time()

    print(count)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
