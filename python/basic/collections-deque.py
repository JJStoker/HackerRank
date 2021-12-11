# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
commands = []
while True:
    try:
        input_cmd = input()
        if not input_cmd:
            break; 
        values = str(input_cmd).split(' ')
        cmd, value = values if len(values) == 2 else [None, None]
        if len(values) == 1:
            try:
                value = int(values[0])
            except ValueError:
                cmd = str(values[0])
        if cmd:
            commands.append([cmd, value])
    except EOFError:
        break;            

for [cmd, value] in commands:
    if not cmd and value:
        d = deque([value])
    elif cmd == 'append':
        if value: d.append(value)
    elif cmd == 'extend':
        if value: d.extend(value)
    elif cmd == 'appendleft':
        if value: d.appendleft(value)
    elif cmd == 'pop':
        d.pop()
    elif cmd == 'popleft':
        d.popleft()
    
print(' '.join(list(d)))

