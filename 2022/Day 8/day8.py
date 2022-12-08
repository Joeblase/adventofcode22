def get_input(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.read().splitlines()
    return input_list


def make_columns(puzzle_input):
    rows = get_input(puzzle_input)
    columns = []
    for char in rows[0]:
        columns.append('')
    for row in rows:
        for char_index, char in enumerate(row):
            columns[char_index] += char
    return columns


def trees(puzzle_input):
    rows = get_input(puzzle_input)
    columns = make_columns(puzzle_input)
    visible = 0
    scores = []
    for r_index, row in enumerate(rows):
        for c_index, char in enumerate(row):
            above = columns[c_index][:r_index][::-1]
            below = columns[c_index][r_index+1:]
            left = row[:c_index][::-1]
            right = row[c_index+1:]
            is_visible = False
            if len(above) == 0 or len(below) == 0 or len(left) == 0 or len(right) == 0:
                is_visible = True
            counter = 0
            for num in above:
                if int(char) <= int(num):
                    counter += 1
                    break
                counter += 1
                if counter == len(above):
                    is_visible = True
            above_score = counter
            counter = 0
            for num in below:
                if int(char) <= int(num):
                    counter += 1
                    break
                counter += 1
                if counter == len(below):
                    is_visible = True
            below_score = counter
            counter = 0
            for num in left:
                if int(char) <= int(num):
                    counter += 1
                    break
                counter += 1
                if counter == len(left):
                    is_visible = True
            left_score = counter
            counter = 0
            for num in right:
                if int(char) <= int(num):
                    counter +=1
                    break
                counter += 1
                if counter == len(right):
                    is_visible = True
            right_score = counter
            if is_visible is True:
                visible += 1
            scores.append(right_score*left_score*above_score*below_score)
    return visible, scores


def amount_visible(puzzle_input):
    return trees(puzzle_input)[0]


def max_score(puzzle_input):
    return max(trees(puzzle_input)[1])


print(f"There are {amount_visible('input.txt')} trees visible from outside the grid")
# There are 1779 trees visible from outside the grid

print(f"The highest score of any tree is: {max_score('input.txt')}")
# The highest score of any tree is: 172224
