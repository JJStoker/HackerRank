# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(list(map(int, input().split(' '))))
balance = 0

for [shoe_size, price] in [
    list(map(int, row.split(' ')))
    for row in [input() for _ in range(int(input()))]
]:
    if shoe_sizes[shoe_size]:
        shoe_sizes[shoe_size] -= 1
        balance += price
print (balance)

