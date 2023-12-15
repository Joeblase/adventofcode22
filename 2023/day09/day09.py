# Created on Dec 15 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/9

import time


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    input_lines = input_string.splitlines()

    sum_end_extrapolations = 0
    sum_front_extrapolations = 0
    for line in input_lines:
        split_line = line.split()
        sequence: list[int] = [int(num) for num in split_line]
        sum_end_extrapolations += extrapolate(sequence, "end")
        sum_front_extrapolations += extrapolate(sequence, "front")

    print(f"Part 1: {sum_end_extrapolations}")
    # Part 1: 1853145119

    print(f"Part 2: {sum_front_extrapolations}")
    # Part 2:


def is_zeros(sequence: list) -> bool:
    for num in sequence:
        if num != 0:
            return False
    return True


def get_differences(sequence: list[int]) -> list[int]:
    new_sequence = []
    i = len(sequence) - 1
    while i >= 1:
        new_sequence.insert(0, sequence[i] - sequence[i - 1])
        i -= 1
    return new_sequence


def extrapolate(sequence: list[int], location: str) -> int:
    sequences: list[list[int]] = [sequence.copy()]

    # calculate arrays of differences
    while not is_zeros(sequences[-1]):
        sequences.append(get_differences(sequences[-1]))

    # extrapolate upward for each array of differences
    i = len(sequences) - 2
    while i >= 0:
        match location:
            case "front":
                sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])
            case "end":
                sequences[i].append(sequences[i][-1] + sequences[i+1][-1])
        i -= 1
    match location:
        case "front":
            return sequences[0][0]
        case "end":
            return sequences[0][-1]


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
