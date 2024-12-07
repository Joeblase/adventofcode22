# Dec 7 2024
# Python 3.13.0

# Advent of Code 2024
# Day 7: Bridge Repair
# https://adventofcode.com/2024/day/7

import time


def is_valid(target, nums, concat=False):
    nums = nums.copy()
    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
    if is_valid(target, [nums[0] * nums[1], *nums[2:]], concat=concat):
        return True
    if is_valid(target, [nums[0] + nums[1], *nums[2:]], concat=concat):
        return True
    if concat:
        if is_valid(
            target, [int(str(nums[0]) + str(nums[1])), *nums[2:]], concat=concat
        ):
            return True


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        input = input_file.read().splitlines()

    res = 0
    res2 = 0
    for line in input:
        target, *nums = [int(x) for x in line.replace(":", " ").split()]
        if is_valid(target, nums):
            res += target
        if is_valid(target, nums, concat=True):
            res2 += target

    # Part 1: 267566105056
    print(f"Part 1: {res}")

    # Part 2: 116094961956019
    print(f"Part 2: {res2}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
