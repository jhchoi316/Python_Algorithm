N = int(input())
T = int(input())
graph = [[] for _ in range(N+1)]
visited=[0]*(N+1)

for i in range(T):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    
def dfs(T):
    visited[T] = 1
    for nx in graph[T]:
        if visited[nx]==0:
            dfs(nx)
            
dfs(1)
print(sum(visited)-1)