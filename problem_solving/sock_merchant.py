#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/
import math
import os
import random
import re
import sys
from functools import reduce


def sockMerchant(n, ar):
    pairs = {}
    num_pairs = 0
    for i in ar:
        if i not in pairs:
            pairs[i] = 1
        else:
            pairs[i] += 1
            if pairs[i] % 2 == 0:
                num_pairs += 1
    return num_pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
