import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())

ice = [list(map(int, read().split())) for i in range(N)]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    iceList = []
    
    while queue:
        x, y = queue.popleft()
        melt = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                if not ice[nx][ny]:
                    melt += 1
                elif ice[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
        if melt > 0:
            iceList.append((x, y, melt))
            
    for x, y, z in iceList:
        ice[x][y] = max(0, ice[x][y]-z)
    
    return 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 0
# 빙산이 있는 구역 저장
iceGraph = []

for i in range(N):
    for j in range(M):
        if ice[i][j]:
            iceGraph.append((i,j))

while iceGraph:
    visited = [[0]*M for _ in range(N)]
    delList = []
    continent = 0
    
    for i, j in iceGraph:
        if ice[i][j] and not visited[i][j]:
            continent += bfs(i,j)
        if ice[i][j] == 0:
            delList.append((i, j))
    if continent > 1:
        print(count)
        break
    
    iceGraph = sorted(list(set(iceGraph) - set(delList)))
    count += 1
    
if continent < 2:
    print(0)