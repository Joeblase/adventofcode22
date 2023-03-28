# Created on Mar 28 2023
# https://adventofcode.com/2015/day/4

import hashlib

try:
    input_file = open('input.txt', 'r')
except FileNotFoundError:
    input_file = open('2015/day04/input.txt', 'r')
input_ = input_file.read()
input_file.close()

def mine_hash(starting_zeros):
    hash_key = input_
    hash_num = 1
    zeros = ''
    for _ in range(starting_zeros):
        zeros += '0'
    while True:
        hash = hashlib.md5((hash_key + str(hash_num)).encode()).hexdigest()
        if hash[:starting_zeros] == zeros:
            return hash_num
        hash_num += 1


print(f"Part 1: {mine_hash(5)}")
# Part 1: 282749

print(f"Part 2: {mine_hash(6)}")
# Part 2: 9962624
