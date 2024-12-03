# Dec 3 2024
# Python 3.13.0

# Advent of Code 2024
# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

import re
import time


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        input = input_file.read()

    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input)

    do = True
    part1 = 0
    part2 = 0
    for instruction in instructions:
        match instruction:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                instruction = instruction.split(",")
                res = int(instruction[0][4:]) * int(instruction[1][:-1])
                part1 += res
                if do:
                    part2 += res

    # Part 1: 174960292
    print(f"Part 1: {part1}")

    # Part 2: 56275602
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
