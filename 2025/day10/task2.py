import collections
import concurrent.futures
import time

count = 0


def input_parser(filename: str) -> list[tuple[str, ...]]:
    with open(filename) as file:
        return [tuple(line.strip().split()) for line in file]


def transform(data):
    new_data = []
    for point in data:
        buttons = [
            frozenset(map(int, button_text[1:-1].split(",")))
            for button_text in point[1:-1]
        ]

        target_joltage = tuple(map(int, point[-1][1:-1].split(",")))

        new_data.append((target_joltage, buttons))

    return new_data


def find_min(point):
    target_joltage, buttons = point
    num_bulbs = len(target_joltage)

    initial_state = tuple([0] * num_bulbs)

    queue = collections.deque([(initial_state, None, 0)])  # (state, prev_button, steps)
    visited = {initial_state}

    while queue:
        current_state, prev_btn, steps = queue.popleft()

        if current_state == target_joltage:
            return steps

        for button in buttons:
            # skip if same as previous button (optimization).
            if button == prev_btn:
                continue

            new_state = list(current_state)
            for bulb_idx in button:
                new_state[bulb_idx] += 1
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, button, steps + 1))

    return float("inf")


def counter(data):
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        results = executor.map(find_min, data)
    return sum(results)


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("data.txt")
    data = transform(data)
    count = counter(data)
    end_time = time.time()

    print(f"Total: {count}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
