# Created on Jan 2 2023
# https://adventofcode.com/2015/day/2

with open('input.txt') as input_file:
    box_dimensions = input_file.read().splitlines()


def calculate_wrapping_paper():
    box_wrapping_paper = []
    for b in box_dimensions:
        b = list(map(int, b.split('x')))
        sides = [b[0]*b[1], b[1]*b[2], b[2]*b[0]]
        box_wrapping_paper.append(2*sum(sides) + min(sides))
    return sum(box_wrapping_paper)


print(f"Part 1: {calculate_wrapping_paper()}")
# 1606483

print(f"Part 2: ")
# 
