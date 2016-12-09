#!/usr/bin/env python3
"""
Tested with:
    echo -e "3\n3\n4\n5" | ./flow018.py

or:
    rerun sh -c "echo -e \"3\n3\n4\n5\" | ./flow018.py"

"""
import math
import sys

# ignore the initial number
next(sys.stdin)

for line in sys.stdin:
    print(math.factorial(int(line)))

