import sys
from collections import deque
sys.setrecursionlimit(10**8)
read = sys.stdin.readline

def bfs(graph, v, visited):
    global count
    queue = deque([v])
    visited[v] = count
    count += 1

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = count
                count += 1

n, m, r = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

bfs(graph, r, visited)

for i in visited[1:]:
    print(i)