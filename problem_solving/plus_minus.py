#!/bin/python3
"""
https://www.hackerrank.com/challenges/plus-minus/
"""
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, length):
    print('\n'.join([
        format(len([i for i in arr if i > 0]) / length, ".6f"),
        format(len([i for i in arr if i < 0]) / length, ".6f"),
        format(len([i for i in arr if i == 0]) / length, ".6f"),
    ]))
    
    pass

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
