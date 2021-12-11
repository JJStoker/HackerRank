# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

groups = defaultdict(list)
size_a, size_b = list(map(int, str(input()).split(' ')))
for x in range(0, size_a):
    n = str(input())
    if len(n) <= 100:
        groups['a'].append(n)
    if x >= 10000:
        break
for x in range(0, size_b):
    n = str(input())
    if len(n) <= 100:
        groups['b'].append(n)
    if x >= 100:
        break

        
for m in groups['b']:
    if m not in groups['a']:
        print('-1')
    else:
        print(' '.join([str(i + 1) for i, d in enumerate(groups['a']) if d == m]))

