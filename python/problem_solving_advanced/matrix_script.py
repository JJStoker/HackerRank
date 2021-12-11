#!/bin/python3

import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(max([0, n])):
    matrix_item = input()
    matrix.append(matrix_item[:min(100, m)])

print(
    re.sub(
        r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])',
        r'\1 ',
        ''.join([''.join(cel) for cel in zip(*matrix)])
    )
)

