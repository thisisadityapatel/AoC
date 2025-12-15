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
        odd_number_lights = set(
            [i for i, value in enumerate(point[0][1:-1]) if value == "#"]
        )
        buttons = []
        for button_text in point[1:-1]:
            buttons.append(set(map(int, button_text[1:-1].split(","))))
        new_data.append([odd_number_lights, buttons])
    return new_data


def find_min(
    point,
):  # dfs backtracking algorithm.
    tracker = []

    def dfs(button_count, path_odd, prev_point, max_iter):
        if button_count >= max_iter:
            return
        if path_odd == point[0]:
            tracker.append(button_count)
            return
        options = point[1]
        if button_count > 0:
            options = []
            for option in point[1]:
                if option != prev_point:
                    options.append(option)
        for option in options:
            new_path_odd = path_odd.symmetric_difference(option)
            dfs(button_count + 1, new_path_odd, option, max_iter)
        return

    for i in range(1, 10):
        dfs(0, set(), set(), i)
        if tracker:
            break
    return min(tracker)


def counter(data):
    count = 0
    for point in data:
        print(point)
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
