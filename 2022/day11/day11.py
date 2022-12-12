# https://adventofcode.com/2022/day/11

# I had to look up how to do part two.
# Multiply the test divisors for each monkey together, item %= that number each inspection

from math import floor, prod

with open('input.txt') as input_file:
    input_ = input_file.read().splitlines()


class Monkey:
    def __init__(self, starting_items, operation, test_div, throw_to_true, throw_to_false):
        self.items = starting_items
        self.operation = operation
        self.test_div = test_div
        self.throw_to_true = throw_to_true
        self.throw_to_false = throw_to_false
        self.items_inspected = 0


def create_monkey_list():
    monkeys = []
    monkey_num = 0
    for line in input_:
        if line[:6] == 'Monkey':
            monkey_index = 0
        if monkey_index == 1:
            starting_items = list(map(int, line[len('  Starting items: '):].split(', ')))
        if monkey_index == 2:
            operation = line[len('  Operation: new = old '):]
        if monkey_index == 3:
            test = int(line[len('  Test: divisible by '):])
        if monkey_index == 4:
            throw_to_true = int(line[-1])
        if monkey_index == 5:
            throw_to_false = int(line[-1])
            # create monkey
            monkeys.append(Monkey(starting_items, operation, test, throw_to_true, throw_to_false))
            monkey_num += 1
        monkey_index += 1
    return monkeys


def do_rounds(num_of_rounds, divide_by_three=True):
    monkey_list = create_monkey_list()
    mod = prod(monkey.test_div for monkey in monkey_list)  # Part 2
    for _ in range(num_of_rounds):
        for monkey in monkey_list:
            for item in monkey.items:
                monkey.items_inspected += 1
                if monkey.operation[2:] == 'old':
                    operation_num = item
                else:
                    operation_num = int(monkey.operation[2:])  # Part 2
                if monkey.operation[0] == '+':
                    item += operation_num
                if monkey.operation[0] == '*':
                    item *= operation_num
                if divide_by_three is True:
                    item = floor(item / 3)
                else:
                    item %= mod
                if item % monkey.test_div == 0:
                    monkey_list[monkey.throw_to_true].items.append(item)
                else:
                    monkey_list[monkey.throw_to_false].items.append(item)
            monkey.items = []
    return monkey_list


def monkey_business(monkey_list):
    items_inspected_list = []
    for monkey in monkey_list:
        items_inspected_list.append(monkey.items_inspected)
    items_inspected_list.sort(reverse=True)
    return items_inspected_list[0] * items_inspected_list[1]


print(f'Part 1: {monkey_business(do_rounds(20))}')
# 118674

print(f'Part 2: {monkey_business(do_rounds(10000, False))}')
# 32333418600
