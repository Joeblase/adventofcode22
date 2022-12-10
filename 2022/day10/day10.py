# https://adventofcode.com/2022/day/10

with open('input.txt') as input_file:
    input_ = input_file.read().splitlines()


def create_screen(w, h):
    screen = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append('.')
        screen.append(row)
    return screen


def screen_list_to_string(screen):
    string = ''
    for row in screen:
        string += ''.join(row) + '\n'
    return string


def draw_pixel(screen, row_index, sprite_position, cycle_num):
    sprite = (sprite_position - 1, sprite_position, sprite_position + 1)
    column_index = (cycle_num - 1) - row_index * 40
    if column_index in sprite:
        screen[row_index][column_index] = '#'
    return screen


def run_program():
    cycle_num, x = 1, 1
    signal_strengths, signal_strength_index = [], 0
    screen, screen_row_index = create_screen(40, 6), 0
    for instruction in input_:
        cycles = 0
        if instruction[:4] == 'noop':
            cycles = 1
        if instruction[:4] == 'addx':
            cycles = 2
        while cycles > 0:
            cycles -= 1
            # during cycle
            if cycle_num == 40 + screen_row_index * 40:
                screen_row_index += 1
            screen = draw_pixel(screen, screen_row_index, x, cycle_num)
            cycle_num += 1  # increment cycle
            # after cycle
            if instruction[:4] == 'addx' and cycles == 0:  # runs after 2 cycles have passed
                x += int(instruction[5:])
            if cycle_num == 20 + signal_strength_index * 40:
                signal_strengths.append(x * cycle_num)
                signal_strength_index += 1
    screen = screen_list_to_string(screen)
    return signal_strengths, screen


print(f'Part 1: {sum(run_program()[0])}')
# Part 1: 13440

print(f'Part 2:\n{run_program()[1]}')
# ###..###..####..##..###...##..####..##..
# #..#.#..#....#.#..#.#..#.#..#....#.#..#.
# #..#.###....#..#....#..#.#..#...#..#..#.
# ###..#..#..#...#.##.###..####..#...####.
# #....#..#.#....#..#.#.#..#..#.#....#..#.
# #....###..####..###.#..#.#..#.####.#..#.
# PBZGRAZA
