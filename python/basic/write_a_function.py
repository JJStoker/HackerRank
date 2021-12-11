# https://www.hackerrank.com/challenges/write-a-function/

def is_leap(year):
    return (
        year % 4 == 0 and
        (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0))
    )
