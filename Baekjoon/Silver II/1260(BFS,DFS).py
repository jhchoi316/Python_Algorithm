import sys
from collections import deque
read = sys.stdin.readline

N, M, V = map(int, read().strip().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, read().strip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def bfs(V):
    queue = deque([V])
    visited[V] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(V):
    visited[V] = True
    print(V, end = " ")

    for i in graph[V]:
        if not visited[i]:
            dfs(i)

visited = [False] * (N + 1)
dfs(V)

print()

visited = [False] * (N + 1)
bfs(V)
