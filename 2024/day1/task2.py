from collections import Counter


def parser(filename: str):
    list1, list2 = [], []
    with open(filename, "r") as file:
        for line in file:
            data = line.split("  ")
            list1.append(int(data[0]))
            list2.append(int(data[1]))
    return list1, list2


if __name__ == "__main__":
    counter = 0
    list1, list2 = parser(filename="data.txt")
    count = Counter(list2)
    for i in range(len(list1)):
        counter += list1[i] * count[list1[i]]
    print(counter)
