from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = support.parse_numbers_split(s)
    for n in numbers:
        pass


    max_index = 0
    max_value = 0
    current_index = 0
    current_value = 0
    lines = s.splitlines()
    for line in lines:
        print(f'{line=}')
        if not line:
            # new elf, move on
            if current_value > max_value:
                max_value = current_value
                max_index = current_index
            
            # incremement our elf and rest count
            current_index += 1
            current_value = 0
        else:
            # same elf
            current_value += int(line)
            print(f'- {current_value=} {current_index=} {max_value=} {max_index=}')

    return max_value


INPUT_S = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
EXPECTED = 24000


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
