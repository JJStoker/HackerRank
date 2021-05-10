# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
letters = ''.join(str(input()).split(' '))
K = int(input())
combines = list(combinations(sorted(letters), K))


print (
    len(list(filter(lambda a: a[0] == 'a', combines))) / 
    len(combines)
)

