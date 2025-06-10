from collections import deque
import sys
read = sys.stdin.readline

def bfs(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    queue = deque([(i,j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                count += 1
    return count

N, M, K = map(int, read().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = []

for i in range(K):
    r, c = map(int, read().split())
    graph[r-1][c-1] = 1
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer.append(bfs(i,j))

print(max(answer))