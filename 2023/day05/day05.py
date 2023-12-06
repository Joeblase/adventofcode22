# Created on Dec 5 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/5

import time
import math


class ConvMap:
    def __init__(self, input_lines_from_map: list = None):
        self.ranges = []
        for line in input_lines_from_map:
            if line == "":
                break
            else:
                split_line = line.split()
                split_line = [int(num) for num in split_line]
                dest_range_start, source_range_start, range_lengths = split_line
                self.ranges.append(ConvRange(dest_range_start, source_range_start, range_lengths))

    def convert_value(self, value: int):
        for conv_range in self.ranges:
            if value in conv_range.source_range:
                offset = value - conv_range.source_range[0]
                return conv_range.dest_range[0] + offset
        return value


class ConvRange:
    def __init__(self, dest_range_start: int, source_range_start: int, range_lengths: int):
        self.dest_range = range(dest_range_start, dest_range_start + range_lengths)
        self.source_range = range(source_range_start, source_range_start + range_lengths)


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    input_lines = input_string.splitlines()
    seeds = input_lines[0].split(":")[1].split()
    seeds = [int(seed) for seed in seeds]
    maps: list[ConvMap] = []

    for line_num, line in enumerate(input_lines):
        if "map" in line:
            maps.append(ConvMap(input_lines[line_num + 1:]))

    # Part 1
    closest_location = math.inf
    for seed in seeds:
        value = seed
        for conv_map in maps:
            value = conv_map.convert_value(value)
        if value < closest_location:
            closest_location = value

    # Part 2
    seed_ranges = []
    i = 0
    while i < len(seeds):
        seed_ranges.append(range(seeds[i], seeds[i]+seeds[i+1]))
        i += 2

    print(f"Part 1: {closest_location}")
    # Part 1: 177942185

    print(f"Part 2: ")
    # Part 2:


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
