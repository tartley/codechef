#!/usr/bin/env python3
"""
Tested with:
    py.test -q --ignore=first_attempt

or:
    rerun py.test -q --ignore=first_attempt

or:
    rerun sh -c "clear; py.test -q --ignore=first_attempt"

"""
import collections
import math
import sys

def read_case(stream):
    num_rows = int(next(stream))
    return [
        [int(i) for i in next(stream).split()]
        for _ in range(num_rows)
    ]

def read_cases(stream):
    num_cases = int(next(stream))
    for _ in range(num_cases):
        yield read_case(stream)

def get_parents(parent_row, index):
    return [
        parent_row[i]
        for i in range(index - 1, index + 1)
        if 0 <= i < len(parent_row)
    ]

def new_maxes(old, row):
    return [
        n + max(get_parents(old, i) + [0])
        for i, n in enumerate(row)
    ]

def get_max_path(case):
    maxes = []
    for row in case:
        maxes = new_maxes(maxes, row)
    return max(maxes)

def main(stream):
    for case in read_cases(stream):
        print(get_max_path(case))

if __name__ == '__main__':
    main(sys.stdin)

