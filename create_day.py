import os
import datetime
import argparse
import webbrowser


def create_template(year, day, now):
    day_name = f"day{day:02d}"
    path = f'{year}/{day_name}'
    link = f"https://adventofcode.com/{year}/day/{day}"

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(f'{path}/input.txt'):
        with open(f'{path}/input.txt', 'w') as _:
            pass
        print(f"Created blank '{path}/input.txt'")

    if not os.path.exists(f'{path}/{day_name}.py'):
        with open(f'{path}/{day_name}.py', 'w') as f:
            f.write(f"""\
# Created on {months[now.month]} {now.day} {now.year}
# {link}

try:
    input_file = open('input.txt', 'r')
except FileNotFoundError:
    input_file = open('{year}/{day_name}/input.txt', 'r')
input_ = input_file.read()
input_file.close()


print(f"Part 1: ")
# 

print(f"Part 2: ")
# 
""")
        print(f"Created template '{path}/{day_name}.py'")
    webbrowser.open(link)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int,
                        help="The year of the Advent of Code")
    parser.add_argument("--day", type=int,
                        help="The day of the Advent of Code")
    args = parser.parse_args()

    now = datetime.datetime.now()
    year = args.year or now.year

    if year < 2015 or year > now.year or (year == now.year and now.month != 12):
        print(f"Invalid year: {year}")
        return

    day = args.day or now.day

    if day not in range(1, 26):
        print(f"Invalid day: {day}")
        return

    create_template(year, day, now)


months = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

if __name__ == "__main__":
    main()
