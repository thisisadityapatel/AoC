import re
import collections
import time

regex_extraction_pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"
processing_time = 0
row_length = 103
col_length = 101


class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return f"Position: {self.position}, Velocity: {(self.velocity)}"

    def move_once(self):
        self.position = (
            (self.position[0] + self.velocity[0]) % col_length,
            (self.position[1] + self.velocity[1]) % row_length,
        )
        return

    def get_position(self):
        return self.position


def extract_values(line):
    match = re.match(regex_extraction_pattern, line)
    if match:
        pos_x = int(match.group(1))
        pos_y = int(match.group(2))
        vel_x = int(match.group(3))
        vel_y = int(match.group(4))
    return (pos_x, pos_y), (vel_x, vel_y)


def get_quadrant_count(positions):
    tracker = collections.defaultdict(list)
    mid_x = col_length // 2
    mid_y = row_length // 2

    for pos in positions:
        x, y = pos
        if 0 <= x < mid_x and 0 <= y < mid_y:  # Upper-left
            tracker["upper_left"].append(pos)
        elif 0 <= x < mid_x and mid_y < y < row_length:  # Lower-left
            tracker["bottom_left"].append(pos)
        elif mid_x < x < col_length and mid_y < y < row_length:  # Lower-right
            tracker["bottom_right"].append(pos)
        elif mid_x < x < col_length and 0 <= y < mid_y:  # Upper-right
            tracker["upper_right"].append(pos)

    prod = 1
    for value in tracker.values():
        prod *= len(value)
    return prod


if __name__ == "__main__":
    start_time = time.time()
    robot_army = []
    data = open("data.txt").read().splitlines()
    for line in data:
        extraction = extract_values(line)
        robot_army.append(Robot(extraction[0], extraction[1]))

    while True:
        processing_time += 1
        for robot in robot_army:
            robot.move_once()
        positions = set()
        flag = True
        for robot in robot_army:
            if tuple(robot.get_position()) in positions:
                flag = False
                break
            positions.add(tuple(robot.get_position()))
        if flag:
            break
    print(processing_time)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.6f} seconds")
