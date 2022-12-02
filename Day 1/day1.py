def elf_calorie_list(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.readlines()

    elf_calories_list = [0]
    elf_index = 0
    for calorie_count in input_list:
        if calorie_count == '\n':
            elf_calories_list.append(0)
            elf_index += 1
        else:
            elf_calories_list[elf_index] += int(calorie_count)
    return elf_calories_list


def top_3_total(puzzle_input):
    elf_calories = elf_calorie_list(puzzle_input)
    elf_calories.sort(reverse=True)
    return sum(elf_calories[0:3])


print(f"The most calories carried by an elf is: {max(elf_calorie_list('input.txt'))}")
# The most calories carried by an elf is: 68787

print(f"The total calories carried by the Elves with the three highest calorie counts is: {top_3_total('input.txt')}")
# The total calories carried by the Elves with the three highest calorie counts is: 198041
