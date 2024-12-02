import os
import re

import requests
from dotenv import load_dotenv


def get_events():

    load_dotenv()
    session_cookie = os.environ["AOC_SESSION_COOKIE"]

    response = requests.get(
        f"https://adventofcode.com/events", cookies={"session": session_cookie}
    )
    if response.ok:
        html = response.text
        html_lines = html.splitlines()
        event_list = []
        for line in html_lines:
            if line[:29] == '<div class="eventlist-event">':
                year = re.search(r"\[(\d{4})]", line).group(1)
                stars = re.search(r"(\d+)\*", line)
                if stars:
                    stars = stars.group(1)
                else:
                    stars = "0"
                event_list.append((year, stars))
        return event_list
    else:
        print(f"ERROR {response.status_code}")


def create_shields(events):
    shields = []
    for event in events:
        year = event[0]
        stars = event[1]

        completion = int(stars) / 50

        color_start = (211, 211, 211)
        color_end = (230, 203, 0)
        color_r = int(color_start[0] + (color_end[0] - color_start[0]) * completion)
        color_g = int(color_start[1] + (color_end[1] - color_start[1]) * completion)
        color_b = int(color_start[2] + (color_end[2] - color_start[2]) * completion)
        color_hex = f"{color_r:02x}{color_g:02x}{color_b:02x}"

        shields.append(
            f"[![{year}](https://img.shields.io/badge/{year}-{stars}★-{color_hex}?style=flat-square)](https://adventofcode.com/{year})"
        )
    return " ".join(shields)


def main():
    events = get_events()
    shields = create_shields(events)
    readme_dir = "docs/README.md"
    with open(readme_dir, "r", encoding="utf-8") as file:
        readme = file.readlines()

    start_index = None
    end_index = None
    for i, line in enumerate(readme):
        if "<!-- SHIELDS_START -->" in line:
            start_index = i
            if end_index is not None:
                break
        if "<!-- SHIELDS_END -->" in line:
            end_index = i
            if start_index is not None:
                break

    if (start_index is not None) and (end_index is not None):
        readme[start_index + 1 : end_index] = shields + "\n"

    with open(readme_dir, "w", encoding="utf-8") as f:
        f.writelines(readme)


if __name__ == "__main__":
    main()
