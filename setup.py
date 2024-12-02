import os
import re

import requests
from dotenv import load_dotenv


def main():

    load_dotenv()
    try:
        session_cookie = os.environ["AOC_SESSION_COOKIE"]
    except KeyError:
        while True:
            print(
                "The session cookie can be retrieved from the headers of any input data request"
            )
            session_cookie = input("Enter session cookie: ")
            if session_cookie == "":
                os._exit(0)
            try:
                response = requests.get("https://adventofcode.com/settings")
                if not response.ok:
                    print("Session cookie not valid")
                else:
                    break
            except Exception as e:
                print(f"There was an error validating the session cookie: {e}")

    with open(".env", "w", encoding="UTF-8") as f:
        f.write(
            f"# The session cookie can be retrieved from the headers of any input data request\nAOC_SESSION_COOKIE={session_cookie}"
        )

    years = []
    for dir_ in os.listdir("."):
        if dir_.isdigit():
            years.append(dir_)

    num_received = 0
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
                            num_received += 1
                        else:
                            raise Exception
                        with open(f"{path}/input.txt", "w", encoding="UTF-8") as f:
                            f.write(input_data)
                    except Exception as e:
                        print(f"There was an error retrieving input data:\n{e}")
    print(f"Retrieved {num_received} input file(s)")


if __name__ == "__main__":
    main()
