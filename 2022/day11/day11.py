# https://adventofcode.com/2022/day/11

from math import floor

with open('input.txt') as input_file:
    input_ = input_file.read().splitlines()


def largest_non_number_factor(number):
    for num in range(1, floor(number/2) + 1):
        if number % num == 0:
            output = num
    return output


class Monkey:
    def __init__(self, starting_items, operation, test, if_true, if_false):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
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
            if_true = int(line[-1])
        if monkey_index == 5:
            if_false = int(line[-1])
            # create monkey
            monkeys.append(Monkey(starting_items, operation, test, if_true, if_false))
            monkey_num += 1
        monkey_index += 1
    return monkeys


def do_rounds(num_of_rounds, divide_by_three=True):
    monkey_list = create_monkey_list()
    for _ in range(num_of_rounds):
        for monkey in monkey_list:
            for item in monkey.items:
                monkey.items_inspected += 1
                if monkey.operation[2:] == 'old':
                    operation_num = item
                else:
                    operation_num = int(monkey.operation[2:])
                if monkey.operation[0] == '+':
                    item += operation_num
                if monkey.operation[0] == '*':
                    item *= operation_num
                if divide_by_three is True:
                    item = floor(item / 3)
                else:
                    pass
                if item % monkey.test == 0:
                    monkey_list[monkey.if_true].items.append(item)
                else:
                    monkey_list[monkey.if_false].items.append(item)
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

#print(f'Part 2: {monkey_business(do_rounds(10000, False))}')
# 
