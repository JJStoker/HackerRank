# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = list(map(int, str(input()).split(' ')))
X = 0

if 1 <= K <= 7 and 1<= M <= 1000:
    nums = []
    for x in range(0, K):
        row = list(map(int, str(input()).split(' ')))
        if 1 <= row[0] <= 7 and len(row) == row[0] + 1:
            nums.append(list(map(lambda x: x ** 2 % M, row[1::])))
    result_m = max(list(map(lambda x: sum(x) % M, product(*nums))))
    if 1 <= result_m <= 10 ** 9:
        X = result_m

print(X)

