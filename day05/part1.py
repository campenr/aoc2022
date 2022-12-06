from __future__ import annotations

import argparse
import os.path
import re
from copy import deepcopy

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _parse_initial_state(initial):

    # setup number of state buckets from last row of initial input.
    state = {int(index): [] for index in initial[-1].split()}
    # add in empty "crates" into gaps so we have continuous data in each line to ease parsing.
    parsed_initial_crates = [
        item.replace('    ', ' [] ').split()
        for item in reversed(initial[:-1])
    ]

    # extract actual values into state
    for line in parsed_initial_crates:
        for index, item in enumerate(line, start=1):
            value = item.replace('[', '').replace(']', '')
            if value:
                state[index].append(value)

    return state


def _split_input(input_: str) -> List[List[int | str]]:
    """Splits input into initial state and movement commands"""
    lines = input_.splitlines()
    initial_state = []
    move_state = []
    parsing_moves = False
    for line in lines:
        if not line:
            parsing_moves = True
        if parsing_moves:
            move_state += [line]
        else:
            initial_state += [line]
    return initial_state, move_state


def compute(s: str) -> int:

    initial_state, moves = _split_input(s)
    stacks = _parse_initial_state(initial_state)

    pattern = 'move (?P<count>[0-9]*) from (?P<src>[0-9]*) to (?P<dest>[0-9]*)'
    for move in moves[1:]:
        # decode move instructions
        match = re.match(pattern, move)
        items = match.groupdict()

        # move items one at a time as per the instructions
        count = int(items['count'])
        for n in range(count):
            value = stacks[int(items['src'])].pop()
            stacks[int(items['dest'])].append(value)

    return ''.join(line[-1] for line in stacks.values())


INPUT_S = '''\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'CMZ'


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
