# Dec 8 2024
# Python 3.13.0

# Advent of Code 2024
# Day 8: Resonant Collinearity
# https://adventofcode.com/2024/day/8

import time
from fractions import Fraction


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        input = input_file.read().splitlines()

    oob = lambda r, c: r < 0 or c < 0 or r >= len(input) or c >= len(input[0])

    map = {}
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char != ".":
                map.setdefault(char, [])
                map[char].append((i, j))

    antinodes = set()
    new_antinodes = set()
    for antennas in map.values():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                a, b = antennas[i], antennas[j]

                # Part 1 Logic
                m = (a[0] - b[0], a[1] - b[1])
                t_a = (a[0] + m[0], a[1] + m[1])
                t_b = (b[0] - m[0], b[1] - m[1])
                if not oob(*t_a):
                    antinodes.add(t_a)
                if not oob(*t_b):
                    antinodes.add(t_b)

                # Part 2 Logic
                m = Fraction(m[0], m[1])
                while not oob(*a):
                    new_antinodes.add(a)
                    a = (a[0] + m.numerator, a[1] + m.denominator)
                while not oob(*b):
                    new_antinodes.add(b)
                    b = (b[0] - m.numerator, b[1] - m.denominator)

    # Part 1: 308
    print(f"Part 1: {len(antinodes)}")

    # Part 2: 1147
    print(f"Part 2: {len(new_antinodes)}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
