elf_choice = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

user_choice = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

round_outcomes = {
    'RR': 3,
    'RP': 6,
    'RS': 0,
    'PR': 0,
    'PP': 3,
    'PS': 6,
    'SR': 6,
    'SP': 0,
    'SS': 3
}

shape_points = {
    'R': 1,
    'P': 2,
    'S': 3
}

player_decision = {
    'RX': 'S',
    'RY': 'R',
    'RZ': 'P',
    'PX': 'R',
    'PY': 'P',
    'PZ': 'S',
    'SX': 'P',
    'SY': 'S',
    'SZ': 'R'
}


def get_input(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.readlines()
    return input_list


def calculate_scores(rpc_rounds):
    scores = []
    for rpc_round in rpc_rounds:
        scores.append(round_outcomes[rpc_round] + shape_points[rpc_round[1]])
    return sum(scores)


def calculate_total_score(puzzle_input):
    input_list = get_input(puzzle_input)
    rpc_rounds = []
    for line in input_list:
        line = line.replace(line[0], elf_choice[line[0]]).replace(line[2], user_choice[line[2]])
        rpc_rounds.append(line[0] + line[2])
    return calculate_scores(rpc_rounds)


def calculate_actual_total_score(puzzle_input):
    input_list = get_input(puzzle_input)
    rpc_rounds = []
    for line in input_list:
        line = line.replace(line[0], elf_choice[line[0]])
        rpc_rounds.append(line[0] + player_decision[line[0]+line[2]])
    return calculate_scores(rpc_rounds)


print(f"Your RPC score is: {calculate_total_score('input.txt')}")
# Your RPC score is: 9177

print(f"Your actual RPC score is: {calculate_actual_total_score('input.txt')}")
# Your actual RPC score is: 12111
