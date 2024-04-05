import sys
from collections import deque 

n = int(sys.stdin.readline())

queue = deque([])

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_back':
        queue.append(int(command[1]))
    elif command[0] == 'push_front':
        queue.appendleft(int(command[1]))
    elif command[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)