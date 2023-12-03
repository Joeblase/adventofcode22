# Created on Dec 3 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/3

import time
import re


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    input_list = input_string.splitlines()
    input_bounds = (len(input_list) - 1, len(input_list[0]) - 1)

    # Part 1:
    part_numbers = []
    for row, line, in enumerate(input_list):
        nums = re.split("[^0-9]+", line)  # creates a list of all numbers
        nums = [num for num in nums if num]  # remove empty elements left by re
        col = 0
        for num in nums:
            # iterate through line until col is the first index of a digit
            while not line[col].isdigit():
                col += 1
            adjacent_locs = get_adjacent(num, row, col, input_bounds)
            for loc in adjacent_locs:
                if input_list[loc[0]][loc[1]] != ".":
                    part_numbers.append(int(num))
                    break
            col += len(num)

    # Part 2:
    gear_ratios = []
    for row, line, in enumerate(input_list):
        for col, c in enumerate(line):
            adjacent_nums = []
            if c == "*":
                # numbers are a minimum of two digits, so there is no need to directly above/below
                offsets = []
                for i in (-1, 0, 1):
                    for j in (-1, 1):
                        offsets.append((i, j))

                # gears can't be on the edge of the grid, so I can index mostly without checking

                # remove a top corner case if a 3-digit number is directly above/below
                for direction in (-1, 1):
                    if input_list[row + direction][col - 1:col + 2].isnumeric():
                        offsets.remove((direction, 1))

                for offset in offsets:
                    if input_list[row + offset[0]][col + offset[1]].isdigit():
                        new_num = [input_list[row + offset[0]][col + offset[1]]]
                        # if we get here we found an adjacent digit, so now just sweep forward and backward
                        # to find remaining digits of the number
                        for direction in (-1, 1):
                            col_sweep = col + offset[1] + direction
                            try:
                                while input_list[row + offset[0]][col_sweep].isdigit():
                                    if direction == -1:
                                        new_num.insert(0, input_list[row + offset[0]][col_sweep])
                                    else:
                                        new_num.append(input_list[row + offset[0]][col_sweep])
                                    col_sweep += direction
                            except IndexError:
                                pass
                        adjacent_nums.append(int(''.join(new_num)))
            if len(adjacent_nums) == 2:
                gear_ratios.append(adjacent_nums[0] * adjacent_nums[1])

    print(f"Part 1: {sum(part_numbers)}")
    # Part 1: 546312

    print(f"Part 2: {sum(gear_ratios)}")
    # Part 2: 87449461


def get_adjacent(string: str, row: int, col: int, input_bounds: tuple) -> list:

    # find all adjacent locations
    str_len = len(string)
    locations = [(row, col - 1), (row, col + str_len)]
    for i in range(col - 1, col + str_len + 1):
        locations.append((row + 1, i))
        locations.append((row - 1, i))

    # filter locations to only valid ones
    valid_locations = []
    for loc in locations:
        if loc[0] < 0 or loc[0] > input_bounds[0]:
            continue
        if loc[1] < 0 or loc[1] > input_bounds[1]:
            continue
        valid_locations.append(loc)
    return valid_locations


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
