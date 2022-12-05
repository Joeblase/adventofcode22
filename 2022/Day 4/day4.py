def get_input(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.read().splitlines()
    return input_list


def break_up_assignments(pair):
    a, b = pair.split(',')[0].split('-'), pair.split(',')[1].split('-')
    a[0], a[1], b[0], b[1] = int(a[0]), int(a[1]), int(b[0]), int(b[1])
    return a, b


def fully_contained_count(puzzle_input):
    assignments = get_input(puzzle_input)
    fully_contained = 0
    for pair in assignments:
        a, b = break_up_assignments(pair)
        if a[0] >= b[0] and a[1] <= b[1]:
            fully_contained += 1
        elif b[0] >= a[0] and b[1] <= a[1]:
            fully_contained += 1
    return fully_contained


def overlap_count(puzzle_input):
    assignments = get_input(puzzle_input)
    overlap_count = 0
    for pair in assignments:
        a, b = break_up_assignments(pair)
        set_a = []
        set_b = []
        for num in range(a[0], a[1]+1):
            set_a.append(num)
        for num in range(b[0], b[1]+1):
            set_b.append(num)
        if sum(set(set_a).intersection(set(set_b))) > 0:
            overlap_count += 1
    return overlap_count


print(f"There are {fully_contained_count('input.txt')} assignment pairs where one range fully contains the other.")
# There are 513 assignment pairs where one range fully contains the other.

print(overlap_count('input.txt'))
# There are 878 assignment pairs that contain overlap
