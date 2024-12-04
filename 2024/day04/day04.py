# Dec 4 2024
# Python 3.13.0

# Advent of Code 2024
# Day 4: Ceres Search
# https://adventofcode.com/2024/day/4

import time
from re import findall, match


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        rows = input_file.read().splitlines()

    n_rows = len(rows)
    n_cols = len(rows[0])
    cols = ["" for _ in range(n_cols)]
    num_diags = n_rows + n_cols
    rdiags = ["" for _ in range(num_diags)]
    ldiags = rdiags.copy()
    for i in range(n_rows):
        for j in range(n_cols):
            cols[j] += rows[i][j]
            ldiags[i + j] += rows[i][j]
            rdiags[i + j] += rows[i][n_cols - 1 - j]

    res = 0
    for line in [*rows, *cols, *rdiags, *ldiags]:
        res += len(findall(r"XMAS", line))
        res += len(findall(r"XMAS", line[::-1]))

    res2 = 0
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            a = match(r"MAS|SAM", rows[i][j] + rows[i + 1][j + 1] + rows[i + 2][j + 2])
            b = match(r"MAS|SAM", rows[i][j + 2] + rows[i + 1][j + 1] + rows[i + 2][j])
            if a and b:
                res2 += 1

    # Part 1: 2507
    print(f"Part 1: {res}")

    # Part 2: 1969
    print(f"Part 2: {res2}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
