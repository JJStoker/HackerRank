def swap_case(s: str):
    return ''.join(map(str.swapcase, list(s)))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
