import datetime
import os

while True:
    year_input = input('Enter year (or press enter for current date): ')
    if str(year_input) == '':
        year = str(datetime.datetime.now().year)
        break
    if int(year_input) in range(2015, datetime.datetime.now().year + 1):
        year = str(year_input)
        break

while True:
    day_input = input('Enter day (or press enter for current date): ')
    if day_input == '':
        day = datetime.datetime.now().day
        break
    if int(day_input) in range(1, 26):
        day = int(day_input)
        break

day_name = 'day'
if day in range(1, 10):
    day_name += '0' + str(day)
else:
    day_name += str(day)

path = f'{year}/{day_name}'

if not os.path.exists(path):
    os.makedirs(path)

if not os.path.exists(f'{path}/input.txt'):
    with open(f'{path}/input.txt', 'w') as _:
        pass
    print(f"Created blank '{path}/input.txt'")

if not os.path.exists(f'{path}/{day_name}.py'):
    with open(f'{path}/{day_name}.py', 'w') as f:
        f.write(
            f"# https://adventofcode.com/{year}/day/{day}\n"
            "\n"
            "with open('input.txt') as input_file:\n"
            "    input_ = input_file.read()\n"
            "\n\n\n"
            "print(f\"Part 1: \")\n"
            "# \n"
            "\n"
            "print(f\"Part 2: \")\n"
            "# \n"
        )
    print(f"Created template '{path}/{day_name}.py'")
