# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = list(map(int, str(input()).split(' ')))
OUTER_BOUNDS = 10 ** 5
OUTER_BOUNDS_NUM = 10 ** 9

def get_nums_from_input(maxLength=None):
    nums = list(
        filter(
            lambda x: 1 <= x <= OUTER_BOUNDS_NUM,
            list(map(int, str(input()).split(' ')))
        )
    )
    return nums[:maxLength] if maxLength else nums

a = get_nums_from_input()
list_A = set(get_nums_from_input(M))
list_B = set(get_nums_from_input(M))

print(
    sum(map(lambda x : -1 if x in list_B else 1 if x in list_A else 0, a))
    if (1 <= N <= OUTER_BOUNDS and 1 <= M <= OUTER_BOUNDS)
    else 0
)

