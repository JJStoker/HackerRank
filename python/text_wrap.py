"""
https://www.hackerrank.com/challenges/text-wrap/
"""
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
