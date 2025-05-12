import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
        
print(count)

