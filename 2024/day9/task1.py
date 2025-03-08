import time
import collections

# Note: brut force approach, havn't yet had the time to refine it


def collect_data(filename):
    return list(map(int, list(open(filename).read())))


def get_fragments(data):
    fragments = []
    num_count = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(data[i]):
                fragments.append(num_count)
            num_count += 1
        else:
            for j in range(data[i]):
                fragments.append(-1)
    return fragments


if __name__ == "__main__":
    start_time = time.time()
    data = collect_data("data.txt")
    fragments = get_fragments(data)
    l, r = 0, len(fragments) - 1
    counter = 0

    while l < r:
        if fragments[l] != -1:
            l += 1
            continue
        if fragments[r] == -1:
            r -= 1
            continue
        fragments[l], fragments[r] = fragments[r], fragments[l]
        l += 1
        r -= 1

    for i in range(len(fragments)):
        value = fragments[i]
        if value != -1:
            counter += i * value

    print(counter)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
