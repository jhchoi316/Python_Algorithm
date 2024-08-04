import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited=[0]*(N+1)
arr = []

for i in range(1,N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(T):
    for i in graph[T]:
        if visited[i] == 0:
            visited[i] = T
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(visited[i])