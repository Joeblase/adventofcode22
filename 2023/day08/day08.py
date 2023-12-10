# Created on Dec 9 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/8

import time


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    input_lines = input_string.splitlines()

    directions = input_lines[0]
    num_directions = len(directions)

    locations = {}
    for line in input_lines[2:]:
        split_line = line.split(',')
        location = (split_line[0][-3:], split_line[1][1:4])
        locations[line[:3]] = location

    # Part 1
    num_moves = 0
    cur_direction = 0
    cur_location = 'AAA'
    while cur_location != 'ZZZ':
        direction = directions[cur_direction]
        cur_location = travel_location(direction, locations, cur_location)
        num_moves += 1
        cur_direction += 1
        cur_direction %= num_directions

    # Part 2
    cur_locations = []
    for location in locations.keys():
        if location[-1] == "A":
            cur_locations.append(location)

    cur_direction = 0
    num_ghost_moves = 0
    while not at_ghost_end(cur_locations):
        for i, location in enumerate(cur_locations):
            direction = directions[cur_direction]
            cur_locations[i] = travel_location(direction, locations, location)
        num_ghost_moves += 1
        cur_direction += 1
        cur_direction %= num_directions
        print(f"{cur_locations} {num_ghost_moves}")

    print(f"Part 1: {num_moves}")
    # Part 1: 21409

    print(f"Part 2: {num_ghost_moves}")
    # Part 2:


def travel_location(direction: str, locations: dict, cur_location: str) -> str:
    match direction:
        case 'L':
            return locations[cur_location][0]
        case 'R':
            return locations[cur_location][1]


def at_ghost_end(cur_locations: list[str]) -> bool:
    for location in cur_locations:
        if location[-1] != "Z":
            return False
    return True


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
