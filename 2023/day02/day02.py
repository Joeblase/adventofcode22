# Created on Dec 2 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/2

import time


class Game:
    def __init__(self, gid: str, gamelog: str):
        self.id = int(gid)
        self.subsets = []
        for subset in gamelog.split("; "):
            self.subsets.append({"red": 0, "green": 0, "blue": 0})
            split_subset = subset.split(", ")  # ex. ['2 green', '6 blue']
            for color in split_subset:
                split_color = color.split()  # ex. ['red', '8']
                self.subsets[-1][split_color[1]] += int(split_color[0])

    def isvalid(self, num_cubes: dict) -> bool:
        for subset in self.subsets:
            for color in subset:
                if subset[color] > num_cubes[color]:
                    return False
        return True

    def get_min_cubes(self) -> dict:
        min_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for subset in self.subsets:
            for color in subset:
                if subset[color] > min_cubes[color]:
                    min_cubes[color] = subset[color]
        return min_cubes


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    games = []
    for line in input_string.splitlines():
        split_line = line.split(': ')
        games.append(Game(split_line[0].split()[1], split_line[1]))

    num_cubes = {
        "red": 12,
        "blue": 14,
        "green": 13
    }

    sum_valid = 0
    for game in games:
        if game.isvalid(num_cubes):
            sum_valid += game.id

    sum_powers = 0
    for game in games:
        min_cubes = game.get_min_cubes()
        power = min_cubes["red"] * min_cubes["blue"] * min_cubes["green"]
        sum_powers += power

    print(f"Part 1: {sum_valid}")
    # Part 1: 2204

    print(f"Part 2: {sum_powers}")
    # Part 2: 71036


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
