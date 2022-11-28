advent of code 2022
===================

https://adventofcode.com/2022

### about

Based on template from [Anthony Sottile](https://github.com/asottile) at [https://github.com/anthonywritescode/aoc2015](https://github.com/anthonywritescode/aoc2015)

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python ./day01/part1.py ./day01/input.txt
74
> 1272 μs
```
