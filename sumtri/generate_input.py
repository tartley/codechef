#!/usr/bin/env python3
import random
import sys

# number of cases (triangles)
print(1)

num_lines = int(sys.argv[1])
print(num_lines)

for line_no in range(1, num_lines + 1):
    print(' '.join(str(random.randint(1, 9)) for i in range(line_no)))

