#!/bin/python3
"""
https://www.hackerrank.com/challenges/mini-max-sum/
"""
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print(" ".join([
        str(sum(sorted(arr)[:4])),
        str(sum(sorted(arr)[-4:])),
    ]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
