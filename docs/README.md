# <img src="assets/favicon.png" alt="favicon" style="width:24px;"> adventofcode <br> <!-- SHIELDS_START -->[![2024](https://img.shields.io/badge/2024-13★-d7d09c?style=flat-square)](https://adventofcode.com/2024) [![2023](https://img.shields.io/badge/2023-16★-d9d08f?style=flat-square)](https://adventofcode.com/2023) [![2022](https://img.shields.io/badge/2022-22★-dbcf76?style=flat-square)](https://adventofcode.com/2022) [![2015](https://img.shields.io/badge/2015-9★-d6d1ad?style=flat-square)](https://adventofcode.com/2015)<!-- SHIELDS_END -->

My Advent of Code solutions.

## Scripts

### setup.py

Creates .env file and downloads input data for previous days.

### create_day.py

Creates a directory and files for a specified day and year, fetches the challenge input data, and opens the corresponding webpage.

Example Usage:\ `python create_day.py --y 2023 --d 1`\ `python create_day.py`
(Uses current date and time)

### update_shields.py

Updates the star shields in `docs/README.md`.
