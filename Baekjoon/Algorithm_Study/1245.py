import sys
from collections import deque
read = sys.stdin.readline

def bfs(i, j):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    queue = deque([(i,j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] <= graph[x][y] and graph[nx][ny] > 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return 1

N, M = map(int, read().split())

graph = [list(map(int, read().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] > 0 and not visited[i][j]:
            answer += bfs(i,j)
print(answer)