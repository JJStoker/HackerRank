"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    high_score = max(arr)
    value = None
    for score in sorted(arr, reverse=True):
        if score < high_score:
            value = score
            break
    print(value)
