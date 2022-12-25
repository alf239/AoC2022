import os.path

import requests


def session_cookie():
    with open("session_cookie.txt", "r") as f:
        return f.read().strip()


def local_cache(day: int):
    return f"input/input_{day:02d}.txt"


def read_input(day: int):
    with open(local_cache(day), "r") as f:
        return f.read()


def get_input(day: int, force: bool = False):
    print(f'get_input(day: {day}, force: {force})')
    url = f'https://adventofcode.com/2022/day/{day}/input'
    target = local_cache(day)
    if os.path.exists(target) and not force:
        print(f'get_input - already have {url} as {target}')
        return read_input(day)
    cookies = {'session': session_cookie()}
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://adventofcode.com/2022/day/{day}/input'
    print(f'get_input - downloading {url} as {target}')
    response = requests.get(url, cookies=cookies, headers=headers)
    with open(target, "w") as f:
        f.write(response.text)
    print(f'get_input - success')
    return read_input(day)


if __name__ == '__main__':
    get_input(3)
