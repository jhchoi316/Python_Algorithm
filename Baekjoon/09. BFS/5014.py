import sys
from collections import deque

# F=최대 높이, S=현재 있는 위치, G=가려고 하는 층수, U,D=위로 아래로 몇 층
F, S, G, U, D = map(int, sys.stdin.readline().split())

# 0~F층까지
visited = [0 for _ in range(F+1)]

def bfs():
    queue = deque()
    queue.append(S)
    visited[S] = 1
    
    while queue: 
        x = queue.popleft()
        
        if x == G:
            return visited[x]-1
        else:
            for y in (x+U, x-D):
                if 0<y<=F and visited[y] == 0:
                    visited[y] = visited[x]+1
                    queue.append(y)
    return "use the stairs"  

print(bfs())