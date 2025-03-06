import sys
from collections import deque
read = sys.stdin.readline

N, M, K, X = map(int, read().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, read().split())
    graph[A].append(B)

distance = [0] * (N+1)
visited = [0] * (N+1)
result = []

def bfs(v, length):
    global result
    queue = deque([v])
    visited[v] = 1
    # 인접한 노드 거리 확인
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[x] + 1
                if distance[i] == length:
                    result.append(i)

bfs(X, K)

if len(result) == 0:
        print(-1)
else:
    result.sort() 
    for i in result:
        print(i)