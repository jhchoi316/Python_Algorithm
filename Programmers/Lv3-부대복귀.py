from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    queue = deque([destination])
    visited[destination] = 0
    
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now]+1
                queue.append(i)

    return [visited[i] for i in sources]