def parser(filename:str):
    list1, list2 = [], []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split("  ")
            list1.append(int(data[0]))
            list2.append(int(data[1]))
    return sorted(list1), sorted(list2)

if __name__ == '__main__':
    list1, list2 = parser(filename="data.txt")
    counter = 0
    for i in range(len(list1)):
        counter += abs(list1[i] - list2[i])
    print(counter)
