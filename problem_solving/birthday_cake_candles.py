#!/bin/python3
"""
https://www.hackerrank.com/challenges/birthday-cake-candles/
"""
import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    max_height = max(ar)
    return len([n for n in ar if n == max_height])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
