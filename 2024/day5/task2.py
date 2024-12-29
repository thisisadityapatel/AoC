import collections
import math


def parser(filename: str):
    with open(filename) as file:
        content = file.read().split("\n")
    index = content.index("")
    return content[:index], content[index + 1 :]


def valid(update) -> bool:
    for i in range(1, len(update)):
        for j in range(0, i):
            if update[j] in rubric[update[i]]:
                return False
    return True


def swap(update):
    for i in range(1, len(update)):
        for j in range(0, i):
            if update[j] in rubric[update[i]]:
                update[i], update[j] = update[j], update[i]
                return update


def resolve(updates) -> int:
    sum = 0
    for update in updates:
        while not valid(update):
            update = swap(update)
        sum += update[math.floor(len(update) / 2)]
    return sum


if __name__ == "__main__":
    rules, updates = parser("data.txt")
    rubric = collections.defaultdict(list)
    incorrect = []

    for rule in rules:
        key, value = map(int, rule.split("|"))
        rubric[key].append(value)

    for update in updates:
        update = list(map(int, update.split(",")))
        if not valid(update):
            incorrect.append(update)

    print(resolve(incorrect))
