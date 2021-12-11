# https://www.hackerrank.com/challenges/merge-the-tools/
import textwrap

def merge_the_tools(string, k):
    parts = list(map(''.join, zip(*[iter(string)]*k)))
    new_string = {}
    for i, part in enumerate(parts):
        new_string[i] = ""
        for s in part:
            if s not in new_string[i]:
                new_string[i] += s
    print('\n'.join(new_string.values()))
