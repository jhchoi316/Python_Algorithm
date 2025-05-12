import sys
read = sys.stdin.readline

def dfs(r):
    global count
    visited[r] = count
    graph[r].sort()
    for i in graph[r]:
        if visited[i] == 0:
            count += 1
            dfs(i)
            
n, m, r = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for i in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range(1, n+1):
    print(visited[i])