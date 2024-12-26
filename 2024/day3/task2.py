import re


def parser(filename: str):
    aggregate_string = []
    with open(filename, "r") as file:
        for line in file:
            aggregate_string.append(line)
    return "".join(aggregate_string)


def get_do_donts_pos(garbage: str):
    do_pos = [m.start() for m in re.finditer(r"do\(\)", garbage)]
    dont_pos = [m.start() for m in re.finditer(r"don't\(\)", garbage)]
    return do_pos, dont_pos


def account_for(do_positions, dont_positions, position):
    closest_do = max([pos for pos in do_positions if pos < position], default=None)
    closest_dont = max([pos for pos in dont_positions if pos < position], default=None)

    if closest_do is None and closest_dont is None:
        return True
    elif closest_do is None:
        return False
    elif closest_dont is None:
        return True
    else:
        return True if position - closest_do < position - closest_dont else False


if __name__ == "__main__":
    garbage = parser("data.txt")
    results = []
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    mul_matches = pattern.findall(garbage)
    mul_positions = [m.start() for m in pattern.finditer(garbage)]
    do_positions, dont_positions = get_do_donts_pos(garbage)

    for i in range(len(mul_positions)):
        if account_for(do_positions, dont_positions, mul_positions[i]):
            num1, num2 = map(int, mul_matches[i])
            results.append(num1 * num2)

    print(sum(results))
