import sys
from collections import deque

read = sys.stdin.readline

def bfs(x, y):
    global graph, n, m, cnt
    visited = [[False]*m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x,y))
    
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = 0
    cnt += 1
    
n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
cnt = 0
count_prev_ones = 0
count_ones = 0

while True:
    count_prev_ones = sum(i.count(1) for i in graph)
    bfs(0,0)
    count_ones = sum(i.count(1) for i in graph)
    
    if count_ones == 0:
        print(cnt)
        print(count_prev_ones)
        break