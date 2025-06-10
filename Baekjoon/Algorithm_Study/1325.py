import sys
from collections import deque
read = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

N, M = map(int, read().split())
computers = [i for i in range(1, N+1)]
graph = [[] for _ in range(0, N+1)]
answer = []
max_count = 0

for i in range(M):
    x, y = map(int, read().split())
    graph[y].append(x)

for i in range(1, N+1):
    visited = [False] * (N+1)
    count = bfs(i)
    max_count = max(max_count, count)
    answer.append((i, count))

for i in answer:
    if i[1] == max_count:
        print(i[0], end = ' ')