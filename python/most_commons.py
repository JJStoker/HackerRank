#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

if __name__ == '__main__':
    counter = defaultdict(int)
    s = input()
    for x in str(s):
        counter[x] += 1

    for c, count in sorted(
        sorted(counter.items(), key=lambda x: x[0]),
        key=lambda j: j[1],
        reverse=True
    )[:3]:
        print(f"{c} {count}")

