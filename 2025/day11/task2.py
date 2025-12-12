import time


def input_parser(filename: str) -> dict:
    data = {}
    with open(filename, "r") as file:
        for line in file:
            temp = line.strip().split(":")
            data[temp[0]] = list(temp[1].strip().split(" "))
    return data


def path_counter(data):
    mem = {}

    def dfs(server, tracker):
        if server == "out":
            return 1 if tracker >= 2 else 0

        key = (server, tracker)
        if key in mem:
            return mem[key]

        outputs = data[server]

        total = 0
        for nxt in outputs:
            if nxt in ("fft", "dac"):
                total += dfs(nxt, tracker + 1)
            else:
                total += dfs(nxt, tracker)

        mem[key] = total
        return total

    return dfs("svr", 0)


if __name__ == "__main__":
    start_time = time.time()
    data = input_parser("data.txt")
    count = path_counter(data)
    end_time = time.time()
    print(count)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
