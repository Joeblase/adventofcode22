import os
import re
import json
import requests


def main():
    with open("session_cookie.json", encoding='UTF-8') as f:
        json_f = json.load(f)
        session_cookie = json_f["SESSION_COOKIE"]

    years = []
    for dir_ in os.listdir("."):
        if re.match("201[5-9]|20[2-9][0-9]|2[1-9][0-9][0-9]", dir_):
            years.append(dir_)

    for year in years:
        for day_path in os.listdir(year):
            if re.match("day(0[1-9]|1[0-9]|2[0-5])", day_path):
                link = f"https://adventofcode.com/{year}/day/{day_path.replace('day', '').lstrip('0')}"
                path = os.path.join(year, day_path)
                if not os.path.exists(f'{path}/input.txt'):
                    try:
                        response = requests.get(f"{link}/input", cookies={'session': session_cookie}, timeout=10)
                        if response.ok:
                            input_data = response.content.decode()
                            print(f"Received day {day_path} year {year}.")
                        else:
                            raise Exception
                        with open(f'{path}/input.txt', 'w', encoding='UTF-8') as f:
                            f.write(input_data)
                    except Exception as e:
                        print(f"There was an error retrieving input data:\n{e}")


if __name__ == "__main__":
    main()
