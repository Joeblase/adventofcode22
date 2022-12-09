def get_input(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.read().splitlines()
    return input_list


def get_stacks(puzzle_input):
    rows = get_input(puzzle_input)[:8]
    stacks = []
    for num in range(1, 10):
        stack = []
        for row in rows:
            item = row[4*num-3]
            if item != ' ':
                stack.insert(0, item)
        stacks.append(stack)
    return stacks


def instruction_numbers(puzzle_input):
    instructions = get_input(puzzle_input)[10:]
    instructions_num = []
    for line in instructions:
        for part in line.split():
            if part.isdigit():
                instructions_num.append(int(part))
    return instructions_num


def move_crates_9000(puzzle_input):
    instructions_num, stacks = instruction_numbers(puzzle_input), get_stacks(puzzle_input)
    num_pos, crate_amount, stack_a, stack_b = 0, 0, 0, 0
    for num in instructions_num:
        if num_pos == 0:
            crate_amount = num
            num_pos += 1
        elif num_pos == 1:
            stack_a = num - 1
            num_pos += 1
        elif num_pos == 2:
            stack_b = num - 1
            while crate_amount > 0:
                stacks[stack_b].append(stacks[stack_a][-1])
                stacks[stack_a].pop()
                crate_amount -= 1
            num_pos = 0
    return stacks


def move_crates_9001(puzzle_input):
    instructions_num, stacks = instruction_numbers(puzzle_input), get_stacks(puzzle_input)
    num_pos, crate_amount, stack_a, stack_b = 0, 0, 0, 0
    for num in instructions_num:
        if num_pos == 0:
            crate_amount = num
            num_pos += 1
        elif num_pos == 1:
            stack_a = num - 1
            num_pos += 1
        elif num_pos == 2:
            stack_b = num - 1
            stacks[stack_b].extend(stacks[stack_a][-crate_amount:])
            del stacks[stack_a][-crate_amount:]
            num_pos = 0
    return stacks


def top_crates(stacks):
    top_crates_, stacks = '', stacks
    for stack in stacks:
        top_crates_ += stack[-1]
    return top_crates_


print(f"The crates on top of the moved stacks are as follows: {top_crates(move_crates_9000('input.txt'))}")
# The crates on top of the moved stacks are as follows: LBLVVTVLP

print(f"The actual crates on top of the moved stacks are as follows: {top_crates(move_crates_9001('input.txt'))}")
#The actual crates on top of the moved stacks are as follows: TPFFBDRJD
