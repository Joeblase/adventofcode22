# Dec 6 2024
# Python 3.13.0

# Advent of Code 2024
# Day 6: Guard Gallivant
# https://adventofcode.com/2024/day/6

import time


def oob(map, r, c):
    return r < 0 or c < 0 or r >= len(map) or c >= len(map[0])


def add_dir(r, c, d):
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    return tuple([sum(x) for x in zip(dirs[d], (r, c))])


def move(map, r, c, d, new_obs=None):
    nr, nc = add_dir(r, c, d)
    if oob(map, nr, nc):
        return None
    while map[nr][nc] == "#" or (nr, nc) == new_obs:
        d = (d + 1) % 4
        nr, nc = add_dir(r, c, d)
    return (nr, nc, d)


def main():

    with open("input.txt", encoding="UTF-8") as input_file:
        map = input_file.read().splitlines()

    for row, line in enumerate(map):
        try:
            start_pos = (row, line.index("^"))
            break
        except ValueError:
            pass
    else:
        raise ValueError("'^' not found")

    # state is a tuple of (current_row, current_col, current_dir)
    cur_state = (*start_pos, 0)
    prev_pos = {start_pos}
    while cur_state:
        cur_state = move(map, *cur_state)
        if cur_state:
            prev_pos.add(cur_state[:2])

    loops = 0
    for r, c in prev_pos:
        cur_state = (*start_pos, 0)
        prev_states = {cur_state}
        if map[r][c] not in "#^":
            while cur_state:
                cur_state = move(map, *cur_state, new_obs=(r, c))
                if cur_state:
                    if cur_state in prev_states:
                        loops += 1
                        break
                    prev_states.add(cur_state)

    # Part 1: 5331
    print(f"Part 1: {len(prev_pos)}")

    # Part 2: 1812
    print(f"Part 2: {loops}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {round(end_time - start_time, 3)} seconds")
