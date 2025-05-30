import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[] for _ in range(N+1)]

def bfs(start, end):
    queue = deque()
    queue.append((start,0))
    visited = [False] * (N+1)
    visited[start] = True
    
    while queue:
        v, d = queue.popleft()
        
        if v == end:
            return d
        
        for i,l in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,d+l))

for i in range(N-1):
    x, y, d = map(int, read().strip().split())
    graph[x].append((y,d)) 
    graph[y].append((x,d))
    
for i in range(M):
    x, y = map(int, read().strip().split())
    print(bfs(x,y))