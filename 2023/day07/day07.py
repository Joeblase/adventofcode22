# Created on Dec 7 2023
# Python 3.12.0
# https://adventofcode.com/2023/day/7

import time
from enum import Enum


class Rank(int, Enum):
    HIGHCARD = 0
    ONEPAIR = 1
    TWOPAIR = 2
    THREEOFAKIND = 3
    FULLHOUSE = 4
    FOUROFAKIND = 5
    FIVEOFAKIND = 6


class Hand:
    card_ranks = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11,
                  "A": 12}

    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.hand_freq = {}
        for char in hand:
            if self.hand_freq.get(char):
                self.hand_freq[char] += 1
            else:
                self.hand_freq[char] = 1
        self.rank = self.get_rank()

    def get_rank(self) -> Rank:
        match max(self.hand_freq.values()):
            case 5:
                return Rank.FIVEOFAKIND
            case 4:
                return Rank.FOUROFAKIND
            case 3:
                if 2 in self.hand_freq.values():
                    return Rank.FULLHOUSE
                return Rank.THREEOFAKIND
            case 2:
                frequencies = list(self.hand_freq.values())
                frequencies.remove(2)
                if 2 in frequencies:
                    return Rank.TWOPAIR
                return Rank.ONEPAIR
            case 1:
                return Rank.HIGHCARD

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        if self.rank > other.rank:
            return False
        for card_i in range(len(self.hand)):
            self_card = self.hand[card_i]
            other_card = other.hand[card_i]
            if self.card_ranks[self_card] < self.card_ranks[other_card]:
                return True
            if self.card_ranks[self_card] > self.card_ranks[other_card]:
                return False


class NewHand(Hand):
    card_ranks = Hand.card_ranks.copy()
    card_ranks['J'] = -1

    def __init__(self, hand: str, bid: int):
        super().__init__(hand, bid)

    def get_rank(self) -> Rank:
        if 'J' in self.hand_freq.keys() and self.hand_freq['J'] != 5:
            freq_no_jokers = self.hand_freq.copy()
            num_jokers = freq_no_jokers.pop('J')
            max_key = max(freq_no_jokers, key=freq_no_jokers.get)
            freq_no_jokers[max_key] += num_jokers
        else:
            freq_no_jokers = self.hand_freq

        match max(freq_no_jokers.values()):
            case 5:
                return Rank.FIVEOFAKIND
            case 4:
                return Rank.FOUROFAKIND
            case 3:
                if 2 in freq_no_jokers.values():
                    return Rank.FULLHOUSE
                return Rank.THREEOFAKIND
            case 2:
                frequencies = list(freq_no_jokers.values())
                frequencies.remove(2)
                if 2 in frequencies:
                    return Rank.TWOPAIR
                return Rank.ONEPAIR
            case 1:
                return Rank.HIGHCARD


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_lines = input_file.readlines()

    print(f"Part 1: {find_winnings(Hand, input_lines)}")
    # Part 1: 252656917

    print(f"Part 2: {find_winnings(NewHand, input_lines)}")
    # Part 2: 253499763


def find_winnings(hand_type, input_lines: list):
    hands = []
    for line in input_lines:
        split_line = line.split()
        hands.append(hand_type(split_line[0], int(split_line[1])))

    hands.sort()

    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand.bid

    return winnings


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 6)} seconds")
