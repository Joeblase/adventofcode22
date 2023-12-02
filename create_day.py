import os
import sys
import datetime
import argparse
import webbrowser
import json
import requests


def create_template(year, day, now):
    day_name = f"day{day:02d}"
    path = f'{year}/{day_name}'
    link = f"https://adventofcode.com/{year}/day/{day}"

    if not os.path.exists(path):
        os.makedirs(path)

    with open("session_cookie.json", encoding='UTF-8') as f:
        json_f = json.load(f)
        session_cookie = json_f["SESSION_COOKIE"]

    if not os.path.exists(f'{path}/input.txt'):
        response = requests.get(f"{link}/input", cookies={'session': session_cookie}, timeout=20)
        input_data = ''
        print(response.status_code)
        if response.ok:
            input_data = response.content.decode()
            print('Received input data')
        with open(f'{path}/input.txt', 'w', encoding='UTF-8') as f:
            f.write(input_data)

    if not os.path.exists(f'{path}/{day_name}.py'):
        with open(f'{path}/{day_name}.py', 'w', encoding='UTF-8') as f:
            f.write(f"""\
# Created on {months[now.month]} {now.day} {now.year}
# Python {sys.version.split(" ")[0]}
# {link}

import time


def main():
    with open('input.txt', encoding='UTF-8') as input_file:
        input_string = input_file.read()

    print(f"Part 1: ")
    # Part 1: 

    print(f"Part 2: ")
    # Part 2: 


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {{round(end_time - start_time, 6)}} seconds")

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
