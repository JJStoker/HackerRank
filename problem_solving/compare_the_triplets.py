#!/bin/python3
# https://www.hackerrank.com/challenges/compare-the-triplets/
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scoreA = 0
    scoreB = 0
    for x in range(len(a)):
        scoreA += 1 if a[x] > b[x] else 0
        scoreB += 1 if a[x] < b[x] else 0
    
    return [scoreA, scoreB]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
