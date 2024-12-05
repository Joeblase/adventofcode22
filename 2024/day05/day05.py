# Dec 5 2024
# Python 3.13.0

# Advent of Code 2024
# Day 5: Print Queue
# https://adventofcode.com/2024/day/5

import time


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        input = input_file.read().splitlines()

    s = input.index("")

    rules = {}
    for rule in input[:s]:
        a, b = map(int, rule.split("|"))
        rules.setdefault(a, set())
        rules[a].add(b)

    res = 0
    res2 = 0
    for update in input[s + 1 :]:
        update = list(map(int, update.split(",")))
        valid_update = True
        prev_pages = {update[0]}
        i = 1
        while i < len(update):
            for rpage in rules.get(update[i], []):
                if rpage in prev_pages:
                    valid_update = False
                    j = update.index(rpage)
                    update[i], update[j] = update[j], update[i]
                    i = j
                    prev_pages = set(update[:i])
                    continue
            prev_pages.add(update[i])
            i += 1
        if valid_update:
            res += update[len(update) // 2]
        else:
            res2 += update[len(update) // 2]

    # Part 1: 6949
    print(f"Part 1: {res}")

    # Part 2: 4145
    print(f"Part 2: {res2}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
