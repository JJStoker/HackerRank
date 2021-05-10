# Enter your code here. Read input from STDIN. Print output to STDOUT
unsorted = str(input())
print(
    ''.join(
        sorted(
            unsorted,
            key=lambda x: (
                -x.islower(),
                x.isdigit() - x.isupper(),
                bool(x.isdigit() and int(x) % 2 == 0),
                x
            ),
        ),
    ) if len(unsorted) <= 1000 else ''
)

