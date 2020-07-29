#!/bin/python3
"""
https://www.hackerrank.com/challenges/designer-pdf-viewer/
"""
import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = 'abcdefghijklmnopqrstuvwxyz';
    word_height = {alpha[i]: j for i, j in enumerate(h)}
    max_height = max(map(lambda x: word_height[x], str(word)))
    return len(word) * max_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
