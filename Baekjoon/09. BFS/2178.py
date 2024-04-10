import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1<nx<N and -1<ny<M and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

    return graph[N-1][M-1]

print(bfs(graph, 0, 0)) 