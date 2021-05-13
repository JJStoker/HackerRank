if __name__ == '__main__':
    arr = []
    N = int(input())
    for line in range(N):
        cmd, *args = str(input()).split()
        if cmd == 'insert':
            if len(args) == 2:
                arr.insert(int(args[0]), int(args[1]))
        elif cmd in ['remove', 'append']:
            if len(args) == 1:
                getattr(arr, cmd)(int(args[0]))
        elif cmd in ['pop']:
            getattr(arr, cmd)()
        elif cmd == 'sort':
            arr = sorted(arr)
        elif cmd == 'reverse':
            arr = list(reversed(arr))
        elif cmd == 'print':
            print(arr)    

