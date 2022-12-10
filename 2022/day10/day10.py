# https://adventofcode.com/2022/day/10

with open('input.txt') as input_file:
    input_ = input_file.read().splitlines()


def get_signal_strengths():
    cycle_num, x = 1, 1
    signal_strengths, signal_strength_index = [], 0
    for instruction in input_:
        cycles = 0
        if instruction[:4] == 'noop':
            cycles = 1
        if instruction[:4] == 'addx':
            cycles = 2
        while cycles > 0:
            cycles -= 1
            cycle_num += 1
            if instruction[:4] == 'addx' and cycles == 0:  # runs after 2 cycles have passed
                x += int(instruction[5:])
            if cycle_num == 20 + signal_strength_index * 40:
                signal_strengths.append(x * cycle_num)
                signal_strength_index += 1
    return signal_strengths


print(f'Part 1: {sum(get_signal_strengths())}')
# Part 1: 13440

print(f'Part 2: ')
# 
