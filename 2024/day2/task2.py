def parser(filename: str):
    store = []
    with open(filename, 'r') as file:
        for line in file:
            store.append(list(map(int, line.split())))
    return store

def validate_report(report):
    dir_flag = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff == 0:
            return False
        if dir_flag == 0:
            dir_flag = 1 if diff > 0 else -1
        if (abs(diff) > 3) or (diff * dir_flag < 0):
            return False
    return True

def problem_dampner(report):
    for i in range(len(report)):
        if validate_report(report[:i] + report[i+1:]):
            return True
    return False

if __name__ == '__main__':
    reports = parser('data.txt')
    counter = 0
    for report in reports:
        if validate_report(report):
            counter += 1
        elif problem_dampner(report):
            counter += 1
    print(counter)

