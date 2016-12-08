#!/usr/bin/env python3
"""
Tested with:
    py.test .

or:
    rerun py.test .

or:
    rerun sh -c "clear; py.test ."

"""
import collections
import math
import sys

class Node:

    def __init__(self, value, *children):
        self.value = value
        self.children = children
        self.left = children[0] if len(children) > 0 else None
        self.right = children[1] if len(children) > 1 else None

def all_paths(node):
    """
    Converts a DAG of nodes into an iterator of paths, eg:

          Node(1)     ->  iter([ [1, 2], [1, 3] ])
           / \
     Node(2) Node(3)

    """
    if node.left or node.right:
        for child in node.children:
            for subpath in all_paths(child):
                yield [node.value] + subpath
    else:
        yield [node.value]

def to_graph(rows):
    """
    Converts lists of values to a graph of Nodes, eg:

        [ [1], [2, 3] ]   ->        Node(1)
                                     / \
                                  left right
                                   /     \
                              Node(2)   Node(3)
    """
    nodes = {}
    for row_idx, row in enumerate(reversed(rows)):
        for index, value in enumerate(row):
            left = None
            right = None
            if row_idx > 0:
                left = nodes[row_idx - 1, index]
                right = nodes[row_idx - 1, index + 1]
            nodes[row_idx, index] = Node(value, left, right)
    return nodes[row_idx, 0]

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

def main(stream):
    for case in read_cases(stream):
        print(max(sum(path) for path in all_paths(to_graph(case))))

if __name__ == '__main__':
    main(sys.stdin)

