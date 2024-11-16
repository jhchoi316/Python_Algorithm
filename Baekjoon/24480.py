import sys
sys.setrecursionlimit(10**8)
read = sys.stdin.readline

def dfs(graph, v, visited):
    global count
    visited[v] = count
    graph[v].sort(reverse=True)
    
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)
            
n, m, r = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
    a, b = map(int,read().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])