import os
import re

import requests
from dotenv import load_dotenv


def main():

    load_dotenv()
    session_cookie = os.environ["AOC_SESSION_COOKIE"]

    years = []
    for dir_ in os.listdir("."):
        if dir_.isdigit():
            years.append(dir_)

    for year in years:
        for day_path in os.listdir(year):
            if re.match("day[0-9]*", day_path):
                link = f"https://adventofcode.com/{year}/day/{day_path.replace('day', '').lstrip('0')}"
                path = os.path.join(year, day_path)
                if not os.path.exists(f"{path}/input.txt"):
                    try:
                        response = requests.get(
                            f"{link}/input",
                            cookies={"session": session_cookie},
                            timeout=10,
                        )
                        if response.ok:
                            input_data = response.content.decode()
                            print(f"Received day {day_path} year {year}.")
                        else:
                            raise Exception
                        with open(f"{path}/input.txt", "w", encoding="UTF-8") as f:
                            f.write(input_data)
                    except Exception as e:
                        print(f"There was an error retrieving input data:\n{e}")


if __name__ == "__main__":
    main()
