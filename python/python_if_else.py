#!/bin/python3
# https://www.hackerrank.com/challenges/py-if-else/
import math
import os
import random
import re
import sys

def check_weird(n):
    print(
        'Not Weird' if (
            n % 2 == 0 and ((2 < n < 5) or (n > 20))
        ) else 'Weird'
    )

if __name__ == '__main__':
    n = int(input().strip())

    check_weird(n)
