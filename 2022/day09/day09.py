def move_head(direction, head_pos):
    if direction == 'U':
        head_pos[1] += 1
    if direction == 'D':
        head_pos[1] -= 1
    if direction == 'L':
        head_pos[0] -= 1
    if direction == 'R':
        head_pos[0] += 1
    return head_pos


def diagonally_touching(a_pos, b_pos):
    if (b_pos[0] == a_pos[0]+1 or b_pos[0] == a_pos[0]-1) and (b_pos[1] == a_pos[1]+1 or b_pos[1] == a_pos[1]-1):
        return True
    if (b_pos[1] == a_pos[1]+1 or b_pos[1] == a_pos[1]-1) and (b_pos[0] == a_pos[0]+1 or b_pos[0] == a_pos[0]-1):
        return True


def move_tail(leading_knot, tail_pos):
    if leading_knot[0] == tail_pos[0]:
        if leading_knot[1] == tail_pos[1] + 2:
            tail_pos[1] += 1
        if leading_knot[1] == tail_pos[1] - 2:
            tail_pos[1] -= 1
    elif leading_knot[1] == tail_pos[1]:
        if leading_knot[0] == tail_pos[0] + 2:
            tail_pos[0] += 1
        if leading_knot[0] == tail_pos[0] - 2:
            tail_pos[0] -= 1
    elif not diagonally_touching(leading_knot, tail_pos):
        if leading_knot[0] > tail_pos[0] and leading_knot[1] > tail_pos[1]:
            tail_pos[0] += 1
            tail_pos[1] += 1
        if leading_knot[0] < tail_pos[0] and leading_knot[1] > tail_pos[1]:
            tail_pos[0] -= 1
            tail_pos[1] += 1
        if leading_knot[0] < tail_pos[0] and leading_knot[1] < tail_pos[1]:
            tail_pos[0] -= 1
            tail_pos[1] -= 1
        if leading_knot[0] > tail_pos[0] and leading_knot[1] < tail_pos[1]:
            tail_pos[0] += 1
            tail_pos[1] -= 1
    return tail_pos


def simulate_movement(puzzle_input, knots):
    with open(puzzle_input) as input_file:
        instructions = input_file.read().splitlines()
    head_pos, tail_positions = [0, 0], []
    [tail_positions.append([0, 0]) for _ in range(knots - 1)]
    previous_end_locations = []
    for line in instructions:
        units = int(line[2:])
        while units > 0:
            head_pos = move_head(line[0], head_pos)
            for i in range(knots - 1):
                if i != 0:
                    tail_positions[i][0] = move_tail(tail_positions[i-1], tail_positions[i])[0]
                    tail_positions[i][1] = move_tail(tail_positions[i - 1], tail_positions[i])[1]
                else:
                    tail_positions[i][0] = move_tail(head_pos, tail_positions[i])[0]
                    tail_positions[i][1] = move_tail(head_pos, tail_positions[i])[1]
            previous_end_locations.append((tail_positions[-1][0], tail_positions[-1][1]))
            units -= 1
    unique_end_locations = []
    for location in previous_end_locations:
        if location not in unique_end_locations:
            unique_end_locations.append(location)
    return unique_end_locations


print(f"The amount of unique locations of the rope's tail with two knots is: {len(simulate_movement('input.txt', 2))}")
# The amount of unique locations of the rope's tail with two knots is: 5779

print(f"The amount of unique locations of the rope's tail with ten knots is: {len(simulate_movement('input.txt', 10))}")
# The amount of unique locations of the rope's tail with ten knots is: 2331
