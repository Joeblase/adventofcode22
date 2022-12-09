def find_floor(puzzle_input):
    with open(puzzle_input) as input_file:
        string = input_file.read()
    floor, enters_basement = 0, ''
    for index, parenthesis in enumerate(string):
        if parenthesis == '(':
            floor += 1
        if parenthesis == ')':
            floor -= 1
        if floor == -1 and isinstance(enters_basement, str):
            enters_basement = index + 1
    return floor, enters_basement


solution = find_floor('input.txt')
print(f"Ending floor: {solution[0]}")
# Ending floor: 74

print(f"Enters basement: {solution[1]}")
# Enters basement: 1795
