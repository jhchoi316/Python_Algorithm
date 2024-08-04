import sys
sys.setrecursionlimit(10**6)

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []

for i in range(1,M+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, num):
    num += 1
    visited[x] = 1
    
    if x == b:
        result.append(num)
    
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i, num)

dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)