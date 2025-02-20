import sys
from collections import deque
read = sys.stdin.readline


def bfs(a, b, map, colour, visited):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque([(a, b)])
    visited[a][b] = 1
    
    while queue:
        x, y = queue.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and map[nx][ny] == colour and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
            
    return 1

N = int(read())
colours = [list(read().strip()) for _ in range(N)]
colours_blind = [['0']*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if colours[i][j] == 'G':
            colours_blind[i][j] = 'R'
        else:
            colours_blind[i][j] = colours[i][j]
            
count0 = 0
count1 = 0
visited0 = [[0]*N for _ in range(N)]
visited1 = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        
        if visited0[i][j] == 0:
            count0 += bfs(i, j, colours, colours[i][j], visited0)

        if visited1[i][j] == 0:
            count1 += bfs(i, j, colours_blind, colours_blind[i][j], visited1)

print(count0, count1)