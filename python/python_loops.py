"""
https://www.hackerrank.com/challenges/python-loops/
"""

if __name__ == '__main__':
    n = int(input())

    for x in range(0, n + 1):
        if x < n < 20:
            print(x * x)