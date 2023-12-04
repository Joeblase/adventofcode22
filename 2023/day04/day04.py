# Created on Dec 4 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/4

import time
from functools import lru_cache


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    input_lines = tuple(input_string.splitlines())
    num_original_cards = len(input_lines)

    # Part 1
    points = 0
    for card_num in range(1, num_original_cards + 1):
        matches = get_matches(card_num, input_lines)
        if matches:
            points += 2 ** (matches - 1)

    # Part 2
    num_cards = 0
    for card_num in range(1, num_original_cards + 1):
        num_cards += process_cards(card_num, input_lines)

    print(f"Part 1: {points}")
    # Part 1: 21158

    print(f"Part 2: {num_cards}")
    # Part 2: 6050769


@lru_cache()
def get_matches(card_num: int, input_lines: tuple) -> int:
    numbers = input_lines[card_num - 1].split(":")[1].split("|")
    my_numbers = numbers[1].split()
    winning_numbers = numbers[0].split()
    matches = 0
    for num in my_numbers:
        if num in winning_numbers:
            matches += 1
    return matches


def process_cards(card_num: int, input_lines: tuple) -> int:
    matches = get_matches(card_num, input_lines)
    num_cards = 1
    if matches:
        for next_card in range(card_num+1, card_num+matches+1):
            num_cards += process_cards(next_card, input_lines)
    return num_cards


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
