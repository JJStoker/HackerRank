VOWELS = ['A', 'E', 'I', 'O', 'U']

def minion_game(string):
    kevin, stuart = 0, 0
    for i in range(len(string)):
        if string[i] in VOWELS:
            stuart += len(string) - i
        else:
            kevin += len(string) - i

    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print('Draw')            

if __name__ == '__main__':
    s = input()
    minion_game(s)
