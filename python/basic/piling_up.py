"""
https://www.hackerrank.com/challenges/piling-up/
might have cheated on this one, can't remember ;-)
"""
from collections import deque

cas = int(input())

for t in range(cas):
    n = int(input())
    queue = deque(map(int,input().split()))
    possible = True
    max_sidelength = (2**31)+1
    while queue:
        sidelength_a = queue[0]
        sidelength_b = queue[-1]
        if sidelength_a >= sidelength_b and max_sidelength >= sidelength_a:
            max_sidelength = queue.popleft()
        elif sidelength_b >= sidelength_a and max_sidelength >= sidelength_b:
            max_sidelength = queue.pop()
        else:
            possible = False
            break
    print('Yes' if possible else 'No')
