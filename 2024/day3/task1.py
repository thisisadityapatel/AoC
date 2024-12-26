import re


def parser(filename: str):
    aggregate_string = []
    with open(filename, "r") as file:
        for line in file:
            aggregate_string.append(line)
    return "".join(aggregate_string)


if __name__ == "__main__":
    garbage = parser("data.txt")

    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(garbage)
    results = []
    for match in matches:
        num1, num2 = map(int, match)
        results.append(num1 * num2)

    print(sum(results))
