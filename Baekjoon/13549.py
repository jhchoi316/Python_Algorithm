import sys
from collections import deque
read = sys.stdin.readline

n, k = map(int, read().split())
time = [0] * 100001

def bfs(n, k, time):
    queue = deque()
    
    if n == 0:
        queue.append(1)
    else:
        queue.append(n)
    
    while queue:
        x = queue.popleft()
        if k == x:
            return time[x]

        for nx in (x-1, x+1, 2*x):
            if 0<=nx<100001 and time[nx]==0:
                if nx == 2*x:
                    time[nx] = time[x]
                    queue.appendleft(nx)
                else:
                    time[nx] = time[x]+1
                    queue.append(nx)

if n == 0:
    if k == 0:
        print(0)
    else:
        print(bfs(n, k, time)+1)
else:
    print(bfs(n,k,time))