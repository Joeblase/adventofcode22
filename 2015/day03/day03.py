# Created on Jan 6 2023
# https://adventofcode.com/2015/day/3

with open('input.txt') as input_file:
    directions = input_file.read()


def move(direction_, visited, location):
    match direction_:
        case '>':
            location[0] += 1
        case 'v':
            location[1] -= 1
        case '<':
            location[0] -= 1
        case '^':
            location[1] += 1
    visited.append(tuple(location)) if tuple(location) not in visited else visited


def part_1():
    location, visited = [0, 0], [(0, 0)]
    for direction in directions:
        move(direction, visited, location)
    return len(visited)


def part_2():
    location_1, location_2, visited = [0, 0], [0, 0], [(0, 0)]
    turn = 0
    for direction in directions:
        match turn:
            case 0:
                move(direction, visited, location_1)
                turn = 1
            case 1:
                move(direction, visited, location_2)
                turn = 0
    return len(visited)


print(f"Part 1: {part_1()}")
# 2565

print(f"Part 2: {part_2()}")
# 2639
