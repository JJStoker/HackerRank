# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for k, g in groupby(map(int, input())):
    print(f'({len(list(g))}, {k})', end=' ')
