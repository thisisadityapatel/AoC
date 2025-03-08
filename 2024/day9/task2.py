import time


def get_data(filename):
    return list(map(int, list(open(filename).read())))


def solve(nums):
    tracker = []
    for i in range(len(nums)):
        if i % 2 != 0:
            tracker.append([None, nums[i]])
        else:
            tracker.append([i // 2, nums[i]])
    i = 0
    while i < len(tracker) - 1:
        i += 1
        position, value = tracker[-i]
        if position:
            for j in range(0, len(tracker) - i):
                if tracker[j][0] == None and tracker[j][1] >= value:
                    if tracker[j][1] == value:
                        tracker[j][0] = position
                        tracker[-i][0] = None
                    else:
                        tracker[-i][0] = None
                        tracker[j][0] = position
                        tracker.insert(j + 1, [None, tracker[j][1] - value])
                        tracker[j][1] = value
                    break
    bitmap = []
    for i in range(len(tracker)):
        for j in range(tracker[i][1]):
            bitmap.append(0 if tracker[i][0] is None else tracker[i][0])

    count = 0
    for i, value in enumerate(bitmap):
        count += i * value
    return count


if __name__ == "__main__":
    start_time = time.time()
    nums = get_data("data.txt")
    answer = solve(nums)
    print(answer)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
