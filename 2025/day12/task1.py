import time


def input_parser(filename: str) -> list:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        i = 0
        parse_shapes = True
        while i < len(lines):
            if parse_shapes and lines[i].strip()[-1] == ":":
                i += 4
            else:
                parse_shapes = False
                # (height, width, shape_total)
                temp = lines[i].strip().split(":")
                rc = temp[0].split("x")
                data.append(
                    (
                        int(rc[0]),
                        int(rc[1]),
                        sum(map(int, temp[1].strip().split(" "))) * 7,
                    )
                )
            i += 1
    return data


def count(data_points):
    count = 0
    for data in data_points:
        height, width, shape_total = data
        if (shape_total / (height * width)) < 0.85:
            count += 1
    return count


if __name__ == "__main__":
    # HINT: each shape is of hte size 7 so im assuming if the given shape is 85 percent filled and 15 percent empty the presents will fit.
    start_time = time.time()
    data_points = input_parser("data.txt")
    print(data_points)
    result = count(data_points)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
