"""
https://www.hackerrank.com/challenges/word-order/
"""

from collections import defaultdict

num_words = int(input())
words = []
for x in range(num_words):
    words.append(str(input().strip('\n')))
counter = defaultdict(int)
for word in words:
    counter[word] += 1
print(len(counter.keys()))
print(' '.join(map(str, counter.values())))
