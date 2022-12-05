from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

ROCK, PAPER, SCISSORS = 1, 2, 3
LOSS, DRAW, WIN = 0, 3, 6
DRAWS = [(ROCK, ROCK), (PAPER, PAPER), (SCISSORS, SCISSORS)]
WINS = [(ROCK, PAPER), (PAPER, SCISSORS), (SCISSORS, ROCK)]
LOSSES = [(ROCK, SCISSORS), (SCISSORS, PAPER), (PAPER, ROCK)]


def parse_move(value):
    match value:
        case 'A' | 'X':
            return ROCK
        case 'B' | 'Y':
            return PAPER
        case 'C' | 'Z':
            return SCISSORS


def compute_match(*them_and_us):
    if them_and_us in DRAWS:
        return DRAW
    elif them_and_us in WINS:
        return WIN
    elif them_and_us in LOSSES:
        return LOSS


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
        them, us = (parse_move(move) for move in line.split())
        result = compute_match(them, us)
        total += result
        total += us

    return total


INPUT_S = '''\
A Y
B X
C Z'''
EXPECTED = 15


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
