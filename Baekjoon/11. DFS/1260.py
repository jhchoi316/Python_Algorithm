from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited1 = [0] * (N+1)

for i in range(1, M+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

result = []

def dfs(x):
    if x not in result:
        visited[x] = 1
        result.append(x)
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

queue = []

def bfs(x):
    queue = deque([x])
    visited1[x] = 1
    while queue:
        x = queue.popleft()
        if x not in result:   
            result.append(x)
        
        for i in graph[x]:
            if visited1[i] == 0:
                visited1[i] = 1
                queue.append(i)

dfs(V)
print(' '.join(map(str, result)))
result = []
bfs(V)
print(' '.join(map(str, result)))