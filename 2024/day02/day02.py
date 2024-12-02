# Dec 2 2024
# Python 3.13.0

# Advent of Code 2024
# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

import time


def main():

    def is_safe(levels):
        for i in range(1, len(levels)):
            diff = levels[i] - levels[i - 1]
            if levels[0] - levels[-1] > 0:
                if diff < -3 or diff > -1:
                    return False
            else:
                if diff > 3 or diff < 1:
                    return False
        return True

    with open("input.txt", encoding="UTF-8") as input_file:
        input = input_file.readlines()

    safe_reports = 0
    pd_safe_reports = 0
    for line in input:
        levels = [int(level) for level in line.split(" ")]
        if is_safe(levels):
            safe_reports += 1
            pd_safe_reports += 1
        else:
            for i in range(len(levels)):
                if is_safe(levels[0:i] + levels[i + 1 :]):
                    pd_safe_reports += 1
                    break

    # Part 1: 486
    print(f"Part 1: {safe_reports}")

    # Part 2: 540
    print(f"Part 2: {pd_safe_reports}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
