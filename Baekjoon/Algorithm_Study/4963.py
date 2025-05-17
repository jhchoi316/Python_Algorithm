import sys
from collections import deque
read = sys.stdin.readline

while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        exit(0)
    graph = [list(map(int,read().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    answer = 0

    def bfs():
        count = 0
        # 우, 좌, 하, 상, 좌상, 좌하, 우하, 우상
        directions = [[0,1], [0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,1], [1,-1]]
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + directions[i][0]
                ny = y + directions[i][1]
                
                if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
        count += 1
        return count
    
    if w == 1 and h == 1:
        if graph[0][0] == 1:
            answer = 1
    else:
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1 and not visited[i][j]:
                    queue = deque([(i,j)])
                    visited[i][j] = True
                    answer += bfs()
    print(answer)