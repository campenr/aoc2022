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

    def update_max(current_value, max_values):
        new_max_values = max_values
        if current_value > max_values[2]:
            new_max_values.append(current_value)
            new_max_values = sorted(new_max_values, reverse=True)
            new_max_values = new_max_values[:3]
        return new_max_values

    max_values = [0, 0, 0]
    current_value = 0
    lines = s.splitlines()
    line_count = len(lines)
    for index, line in enumerate(lines, start=1):

        try:
            # increment calories for current elf
            current_value += int(line)
        except ValueError:
            # new elf, update max if needed, and move on
            max_values = update_max(current_value, max_values)
            # reset our value count
            current_value = 0

    # one last time for the last row of data
    max_values = update_max(current_value, max_values)

    return sum(max_values)


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
EXPECTED = 45000


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
