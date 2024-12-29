import collections
import math


def parser(filename: str):
    with open(filename) as file:
        content = file.read().split("\n")
    index = content.index("")
    return content[:index], content[index + 1 :]


if __name__ == "__main__":
    rules, updates = parser("data.txt")
    rubric = collections.defaultdict(list)
    correct_updates = []

    for rule in rules:
        key, value = map(int, rule.split("|"))
        rubric[key].append(value)

    for update in updates:
        update = list(map(int, update.split(",")))
        run_flag = 0
        for i in range(1, len(update)):
            if run_flag == 0:
                for j in range(0, i):
                    if update[j] in rubric[update[i]]:
                        run_flag = 1
                        break
        if run_flag == 0:
            correct_updates.append(update)

    sum = 0
    for update in correct_updates:
        sum += update[math.floor(len(update) / 2)]

    print(sum)
