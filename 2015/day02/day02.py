# Created on Jan 2 2023
# https://adventofcode.com/2015/day/2

with open('input.txt') as input_file:
    box_dimensions = input_file.read().splitlines()


def calculate_wrapping_paper(ribbon=False):
    box_wrapping_paper = []
    box_ribbon = []
    for box in box_dimensions:
        box = list(map(int, box.split('x')))
        box.sort()
        side_areas = [box[0]*box[1], box[1]*box[2], box[2]*box[0]]
        if ribbon is False:
            box_wrapping_paper.append(2*sum(side_areas) + min(side_areas))
        else:
            box_ribbon.append(box[0]*2 + box[1]*2 + box[0]*box[1]*box[2])
    if ribbon is False:
        return sum(box_wrapping_paper)
    else:
        return sum(box_ribbon)


print(f"Part 1: {calculate_wrapping_paper()}")
# 1606483

print(f"Part 2: {calculate_wrapping_paper(True)}")
# 3858306
