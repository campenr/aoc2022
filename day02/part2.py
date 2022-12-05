from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

ROCK, PAPER, SCISSORS = 1, 2, 3
LOSS, DRAW, WIN = 0, 3, 6


def parse_move(value):
    match value:
        case 'A':
            return ROCK
        case 'B':
            return PAPER
        case 'C':
           return SCISSORS

def parse_result(result):
    match result:
        case 'X':
            return LOSS
        case 'Y':
            return DRAW
        case 'Z':
           return WIN

def compute_play(them, result):
    # this is effectively the same logic as the module approach. A cirlce of results with 3 wrapping around to 1. I just can't get the module logic to work. :shrug:
    if result == DRAW:
        us = them
    if result == LOSS:
        us = them - 1
        if us < 1: us = 3
    if result == WIN:
        us = them + 1
        if us > 3: us = 1
    return us

def compute(s: str) -> int:

    """
    I know there's a fancier solution using modulo, or I could just map the inputs for a match to
    the score for that match, but my brain isn't working right and can't get either to work, so here
    we are using branching and pattern matching. A good time to play with 3.10's pattern matching
    if nothing else.
    """

    total = 0

    lines = s.splitlines()
    for line in lines:
        them, result = parse_move(line[0]), parse_result(line[-1])
        us = compute_play(them, result)
        total += result
        total += us

    return total


INPUT_S = '''\
A Y
B X
C Z'''
EXPECTED = 12


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
