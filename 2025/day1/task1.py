from turtle import pos


def parser(filename: str):
    content = []
    with open(filename) as file:
        content = file.read().split("\n")
    return content

if __name__ == "__main__":
    actions = parser("data.txt")
    counter = 0
    position = 50
    for action in actions:
        direction, change = action[0], int(action[1:])
        if direction == 'L':
            position = (position - change) % 100
        else:
            position = (position + change) % 100
        if position == 0:
            counter += 1
    print(counter)