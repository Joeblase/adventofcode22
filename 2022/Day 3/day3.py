alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_input(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.read().splitlines()
    return input_list


def find_duplicate_characters(puzzle_input):
    rucksack_list = get_input(puzzle_input)
    duplicate_characters = []
    for rucksack in rucksack_list:
        half_length = int(len(rucksack)/2)
        comp_1 = rucksack[:half_length]
        comp_2 = rucksack[half_length:]
        for char in comp_1:
            if char in comp_2:
                duplicate_characters.append(char)
                break
    return duplicate_characters


def get_char_priorities(list_):
    char_list = list_
    priorities_list = []
    for char in char_list:
        priorities_list.append(alphabet.find(char))
    return priorities_list


def intersection(str1, str2, str3):
    intersection_ = [char for char in str1 if char in str2 and char in str3]
    return intersection_[0]


def find_group_characters(puzzle_input):
    rucksack_list = get_input(puzzle_input)
    rucksack_total = len(rucksack_list)
    group_characters = []
    while rucksack_total > 0:
        group = rucksack_list[rucksack_total-3: rucksack_total]
        group_characters.append(intersection(group[0], group[1], group[2]))
        rucksack_total += -3
    return ''.join(group_characters)


print(f"The sum of the priorities of the duplicate item types is: "
      f"{sum(get_char_priorities(find_duplicate_characters('input.txt')))}")
# The sum of the priorities of the duplicate item types is: 7674

print(f"The sum of the priorities of the item type for each group badge is: "
      f"{sum(get_char_priorities(find_group_characters('input.txt')))}")
# The sum of the priorities of the duplicate item types is: 7674
