# Created on Dec 7 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/6

import time


class Race:
    def __init__(self, rtime: str, distance: str):
        self.time = int(rtime)
        self.record_distance = int(distance)

    def num_ways_to_win(self):
        sum_ways = 0
        for i in range(self.time + 1):
            speed = i
            remaining_time = self.time - i
            distance_traveled = speed * remaining_time
            if distance_traveled > self.record_distance:
                sum_ways += 1
        return sum_ways


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_lines = input_file.readlines()

    times = input_lines[0].split()[1:]
    distances = input_lines[1].split()[1:]

    # Part 1
    races = []
    for i in range(len(times)):
        races.append(Race(times[i], distances[i]))

    product_ways_to_win = 1
    for race in races:
        product_ways_to_win *= race.num_ways_to_win()

    # Part 2
    real_race = Race(''.join(times), ''.join(distances))

    print(f"Part 1: {product_ways_to_win}")
    # Part 1: 2344708

    print(f"Part 2: {real_race.num_ways_to_win()}")
    # Part 2: 30125202


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
