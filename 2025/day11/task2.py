import time


def input_parser(filename: str) -> dict:
    data = {}
    with open(filename, "r") as file:
        for line in file:
            temp = line.strip().split(":")
            data[temp[0]] = list(temp[1].strip().split(" "))
    return data


def path_counter(data):
    count = 0

    def dfs(server, tracker):
        outputs = data[server]
        if "out" in outputs:
            if tracker >= 2:
                nonlocal count
                count += 1
            return
        flag = False
        for output in outputs:
            if output in ["fft", "dac"]:
                flag = flag or dfs(output, tracker + 1)
            else:
                flag = flag or dfs(output, tracker)
        return flag

    dfs("svr", 0)
    return count


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("test.txt")
    count = path_counter(data)
    end_time = time.time()
    print(count)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
