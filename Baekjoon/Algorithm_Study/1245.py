import sys
from collections import deque
read = sys.stdin.readline

def bfs(i, j):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    queue = deque([(i, j)])
    visited[i][j] = True
    is_peak = True
    current_height = graph[i][j]

    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] > current_height:
                    is_peak = False
                if not visited[nx][ny] and graph[nx][ny] == current_height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    if is_peak:
        return 1
    else:
        return 0

N, M = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0 and not visited[i][j]:
            answer += bfs(i, j)
print(answer)
