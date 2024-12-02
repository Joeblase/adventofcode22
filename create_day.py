import argparse
import datetime
import os
import re
import sys
import webbrowser

import requests
from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--y", type=int, help="The year of the Advent of Code")
    parser.add_argument("--d", type=int, help="The day of the Advent of Code")
    parser.add_argument("--t", type=str, help="The template to use from /templates")
    args = parser.parse_args()

    now = datetime.datetime.now()
    year = args.y or now.year
    day = args.d or now.day
    try:
        template = os.environ["AOC_DEFAULT_TEMPLATE"]
    except KeyError:
        template = "python"
    template = args.t or template

    if not os.path.exists(f"templates/{template}.txt"):
        print(f"Template {template} not found")
        os._exit(1)

    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }

    day_name = f"day{day:02d}"
    path = f"{year}/{day_name}"
    link = f"https://adventofcode.com/{year}/day/{day}"

    try:
        response = requests.get(link, timeout=10)
        if response.ok:
            html = response.text
        else:
            print(f"Invalid day ({day}) and/or year ({year})")
            raise Exception
    except Exception as e:
        print(f"There was an error fetching the problem\n{e}")
        os._exit(1)

    day_title = ""
    res = re.search("--- Day [0-9]*: .* ---", html)
    if res:
        res = res.group(0)
        day_title = res.strip(" -").split(":")[1].strip()

    template_vars = {
        "date": f"{months[now.month]} {now.day} {now.year}",
        "day": day,
        "link": link,
        "python_version": sys.version.split(" ")[0],
        "title": day_title,
        "year": year,
    }

    if not os.path.exists(path):
        os.makedirs(path)

    load_dotenv()
    session_cookie = os.environ["AOC_SESSION_COOKIE"]

    if not os.path.exists(f"{path}/input.txt"):
        input_data = ""
        try:
            response = requests.get(
                f"{link}/input", cookies={"session": session_cookie}, timeout=10
            )
            if response.ok:
                input_data = response.content.decode()
            else:
                raise Exception
        except Exception as e:
            print(f"There was an error retrieving input data:\n{e}")

        with open(f"{path}/input.txt", "w", encoding="UTF-8") as f:
            f.write(input_data)

    if not os.path.exists(f"{path}/{day_name}.py"):
        with open(f"{path}/{day_name}.py", "w", encoding="UTF-8") as new_file:
            with open(f"templates/{template}.txt", "r", encoding="UTF-8") as template_f:
                template = template_f.read()
            new_file.write(template.format(**template_vars))
        print(f"Created template '{path}/{day_name}.py'")
    webbrowser.open(link)


if __name__ == "__main__":
    main()
