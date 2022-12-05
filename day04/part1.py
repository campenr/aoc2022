from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    result = 0
    lines = s.splitlines()
    for line in lines:
        first, second = line.split(',')

        first = first.split('-')
        first = set(range(int(first[0]), int(first[1]) + 1))

        second = second.split('-')
        second = set(range(int(second[0]), int(second[1]) + 1))

        intersect = first.intersection(second)
        fully_contains = len(intersect) == len(first) or len(intersect) == len(second)

        if fully_contains:
            result += 1

    return result


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 2


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
