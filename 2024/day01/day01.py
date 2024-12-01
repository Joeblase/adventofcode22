# Created on Dec 1 2024
# Python 3.13.0
# https://adventofcode.com/2024/day/1

import time


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        input = input_file.readlines()

    list_a = []
    list_b = []
    for line in input:
        split_line = line.split("   ")
        list_a.append(int(split_line[0]))
        list_b.append(int(split_line[1]))

    list_a.sort()
    list_b.sort()

    total_dist = 0
    for i in range(len(input)):
        total_dist += abs(list_a[i] - list_b[i])

    similarity_score = 0
    for num in list_a:
        apps = 0  # there are no duplicates so this can be reset for every number
        while list_b and num >= list_b[0]:
            if list_b[0] == num:
                apps += 1
            list_b.pop(0)
        similarity_score += num * apps

    print(f"Part 1: {total_dist}")
    # Part 1: 2176849

    print(f"Part 2: {similarity_score}")
    # Part 2: 23384288


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
