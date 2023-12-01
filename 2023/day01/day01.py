# Created on Dec 1 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/1

import time


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    digits_only = ''.join(c for c in input_string if (c.isdigit() or c == "\n"))
    sum1 = 0
    for line in digits_only.split('\n'):
        sum1 += int(line[0] + line[-1])

    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    new_input_string = ""
    i = 0
    while i < len(input_string):
        string_digit = False
        for length in {3, 4, 5}:
            if input_string[i:i + length] in digits.keys():
                new_input_string += digits[input_string[i:i + length]]
                string_digit = True
                break
        if not string_digit:
            new_input_string += input_string[i]
        i += 1

    new_digits_only = ''.join(c for c in new_input_string if (c.isdigit() or c == "\n"))
    sum2 = 0
    for line in new_digits_only.split('\n'):
        sum2 += int(line[0] + line[-1])

    print(f"Part 1: {sum1}")
    # Part 1: 54081

    print(f"Part 2: {sum2}")
    # Part 2: 54649


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
