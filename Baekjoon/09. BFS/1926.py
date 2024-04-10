import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상하좌우 좌표 선언
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    # 방문해야할 정보를 담은 queue 선언
    queue = deque()
    queue.append([a,b])
    graph[a][b] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그림 범위 안이고, 그림이 있다면
            if -1<nx<N and -1<ny<M and graph[nx][ny]==1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1
                
    return count

res = []
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            res.append(bfs(graph, i, j))

if len(res) == 0:
    print(len(res))
    print(0)
else:
    print(len(res))
    print(max(res))