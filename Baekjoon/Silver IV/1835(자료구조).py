import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
result = deque()

for i in range(n, 0, -1):
    result.appendleft(i)
    if i < n:
        for j in range(i):
            result.appendleft(result.pop())
        
    if len(result)==n:
        print(*result, end=" ")
        break