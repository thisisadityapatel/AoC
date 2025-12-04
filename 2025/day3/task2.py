import time


def input_parser(filename: str) -> list[str]:
    banks = []
    try:
        with open(filename) as file:
            banks = file.read().strip().split("\n")
    except Exception as e:
        print(e)
    return banks


def get_max_and_position(nums: str):
    max_val = int(nums[0])
    max_index = 0
    for i in range(0, len(nums)):
        if max_val < int(nums[i]):
            max_val = int(nums[i])
            max_index = i
    return max_val, max_index


def max_jolt(bank: str) -> int:
    current_numbers = bank[len(bank) - 12 :]
    choice_numbers = bank[: len(bank) - 12]
    max_number = ""
    while len(max_number) != 12:
        head = int(current_numbers[0])
        if not choice_numbers or not current_numbers:
            new_size = 12 - len(max_number)
            new_array = choice_numbers if not current_numbers else current_numbers
            if new_size == len(new_array):
                max_number += new_array
                break
            current_numbers = new_array[len(new_array) - new_size :]
            choice_numbers = new_array[: len(new_array) - new_size]
            continue
        max_val, max_index = get_max_and_position(choice_numbers)
        if max_val >= head:
            max_number += str(max_val)
            choice_numbers = choice_numbers[max_index + 1 :] + current_numbers[0]
            current_numbers = current_numbers[1:]
        else:
            max_number += str(head)
            choice_numbers = ""
            current_numbers = current_numbers[1:]
    return int(max_number)


def solve(banks: list[str]) -> int:
    total = 0
    for bank in banks:
        total += max_jolt(bank)
    return total


if __name__ == "__main__":
    start_time = time.time()
    banks = input_parser("data.txt")
    result = solve(banks)
    end_time = time.time()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")
