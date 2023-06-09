from __future__ import annotations

import argparse
import os.path

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Node(object):

     def __init__(self, name, address, parent=None):
         self.name = name
         self.address = address
         self.parent = parent
         self.children = []

def _parse_in(command):
    return [item.strip() for item in command.strip().split(' ')]


def _handle_output(command, *lines):
    print(f'{command=} {lines=}')


def _build_tree(input):

    # tree things
    tree = Node('/', 0)
    current_node = tree
    flat = ('/',)

    # i/o state
    out_buffer = []
    command, *args = None, []
    read_mode = False

    for line in input:

        if line.startswith('$'):
            # set flag to indicate read mode has ended, and parse command for later usage
            # after we handle any output from the a previous command.
            read_mode = False
            command, *args = _parse_in(line[1:])

        if read_mode:
            out_buffer.append(line)
        else:
            if len(out_buffer):
                _handle_output(command, out_buffer)
                out_buffer = []
            if command == 'cd':
                dirname = args[0]
                if dirname == '..':
                    current_node = current_node.parent
                else:
                    # move to new node
                    new_node = Node(dirname,   current_node)
                    current_node.children.append(new_node)
                    current_node = new_node
            if command == 'ls':
                pass  # await output

        # prepare for next line, if its a command we'll catch it at the start of the next loop.
        read_mode = True


def compute(s: str) -> int:

    lines = s.splitlines()
    tree = _build_tree(s.splitlines())

    return 0


INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 95437


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
