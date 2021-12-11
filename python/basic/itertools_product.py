from itertools import product

list_a = list(map(int, str(input()).split(' ')))
list_b = list(map(int, str(input()).split(' ')))
print(' '.join(map(str, product(*[list_a, list_b]))))
