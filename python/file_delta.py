#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    try:
        datetime_t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
        datetime_t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
        assert datetime_t1.year <= 3000
        assert datetime_t2.year <= 3000
        if datetime_t1 > datetime_t2:
            return str(int((datetime_t1 - datetime_t2).total_seconds()))
            
        return str(int((datetime_t2 - datetime_t1).total_seconds()))
    except:
        return
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
